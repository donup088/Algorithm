import sys
input = sys.stdin.readline
from collections import deque

dx=[-1,0,1,0]
dy=[0,1,0,-1]

t=int(input())

def bfs(cx,cy):
  q=deque()
  q.append([cx,cy])
  visited[cx][cy]=1
  while q:
    x,y=q.popleft()
    for i in range(4):
      xx=x+dx[i]
      yy=y+dy[i]
      if 0<=xx<n and 0<=yy<m and visited[xx][yy]==0 and [xx,yy] in b:
        q.append([xx,yy])
        visited[xx][yy]=1
  
for _ in range(t):
  b=[]
  #가로 m 세로 n
  m,n,k=map(int,input().split())
  count=0
  for _ in range(k):
    x,y=map(int,input().split())
    b.append([y,x])
  visited=[[0]*m for _ in range(n)]
  for x,y in b:
    if visited[x][y]==0:
      count+=1
      bfs(x,y)

  print(count)