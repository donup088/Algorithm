import sys
from collections import deque

dx=[0,1,0,-1]
dy=[1,0,-1,0]

def bfs(cx,cy,h):
  q=deque()
  q.append([cx,cy])
  visited[cx][cy]=1
  while q:
    x,y=q.popleft()
    for i in range(4):
      xx,yy=x+dx[i],y+dy[i]
      if 0<=xx<n and 0<=yy<n and board[xx][yy]>h and visited[xx][yy]==0:
        q.append([xx,yy])
        visited[xx][yy]=1
      
n=int(input())
board=[]
set_board=set()
answer=[]
set_board.add(0)
for _ in range(n):
  b=list(map(int,input().split()))
  for i in range(len(b)):
    set_board.add(b[i])
  board.append(b)
  
for x in set_board:
  visited=[[0]*n for _ in range(n)]
  count=0
  for i in range(n):
    for j in range(n):
      if visited[i][j]==0 and board[i][j]>x:
        count+=1
        bfs(i,j,x)
  answer.append(count)

print(max(answer))