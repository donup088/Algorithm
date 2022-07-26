import sys
input = sys.stdin.readline
from collections import deque

dx=[-1,0,1,0,1,1,-1,-1]
dy=[0,1,0,-1,1,-1,1,-1]

def bfs(cx,cy):
  q=deque()
  q.append([cx,cy])
  visited[cx][cy]=1
  while q:
    x,y=q.popleft()
    for i in range(8):
      xx,yy=x+dx[i],y+dy[i]
      if 0<=xx<h and 0<=yy<w and visited[xx][yy]==0 and board[xx][yy]==1:
        q.append([xx,yy])
        visited[xx][yy]=1

while True:
  w,h=map(int,input().split())
  if w==0 and h==0:
    break
    
  board=[list(map(int,input().split())) for _ in range(h)]
  visited=[[0]* w for _ in range(h)]
  count=0
  
  for i in range(h):
    for j in range(w):
      if board[i][j]==1 and visited[i][j]==0:
        count+=1
        bfs(i,j)
  print(count)