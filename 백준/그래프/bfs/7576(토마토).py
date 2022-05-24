from collections import deque
dx=[-1,0,1,0]
dy=[0,1,0,-1]
# M 가로 N 세로
M,N=map(int,input().split())
box=[list(map(int,input().split())) for _ in range(N)]
start=[]
res=0
for i in range(M):
  for j in range(N):
    if box[j][i]==1:
      start.append((j,i))

q=deque()
for i in range(len(start)):
  q.append((start[i]))
while q:
  y,x=q.popleft() # y 세로 x 가로
  for i in range(4):
    xx=x+dx[i]
    yy=y+dy[i]
    if 0<=xx<M and 0<=yy<N and box[yy][xx]==0:
      q.append((yy,xx))
      box[yy][xx]=box[y][x]+1
      
for i in range(M):
  for j in range(N):
    if box[j][i]==0:
      print(-1)
      exit(0)
    res=max(res,box[j][i])
print(res-1)