from collections import deque

dx=[1,0,-1,0]
dy=[0,1,0,-1]

c,r=map(int,input().split())
board=[list(map(int,input().split())) for _ in range(c)]
res=[]

def bfs():
  visited=[[0]*r for _ in range(c)]
  visited[0][0]=1
  cnt=0
  q=deque()
  q.append([0,0])
  while q:
    x,y=q.popleft()
    for i in range(4):
      xx=x+dx[i]
      yy=y+dy[i]
      if 0<=xx<c and 0<=yy<r and visited[xx][yy]==0:
        if board[xx][yy]==0:
          visited[xx][yy]=1
          q.append([xx,yy])
        elif board[xx][yy]==1:
          board[xx][yy]=0
          visited[xx][yy]=1
          cnt+=1
  res.append(cnt)
  return cnt

t=0

while True:
  cnt=bfs()
  if cnt==0:
    break
  t+=1
print(t)
print(res[-2])