from collections import deque

dx=[-1,0,1,0]
dy=[0,1,0,-1]
N,H,D=map(int,input().split())

def bfs():
  q=deque()
  q.append((cx,cy,0,H,0))
  visited = [[0]*N for _ in range(N)]
  visited[cx][cy]=H
  while q:
    x,y,u,h,cnt=q.popleft()
    for i in range(4):
      xx=x+dx[i]
      yy=y+dy[i]
      if 0<=xx<N and 0<=yy<N :
        if m[xx][yy]=='E':
          return cnt+1

        nh, nd = h, u

        if m[xx][yy]=='U':
          nd=D
        if nd>0:
          nd-=1
        else:
          nh-=1
        if nh > visited[xx][yy]:
          visited[xx][yy] = nh
          q.append((xx, yy, nd, nh, cnt + 1))
  return -1

m=[]
cx,cy=0,0
for i in range(N):
  m.append(list(input()))
for i in range(N):
  for j in range(N):
    if m[i][j]=='S':
      cx,cy=i,j

print(bfs())