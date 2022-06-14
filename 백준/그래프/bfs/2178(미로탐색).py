import sys
from collections import deque

input = sys.stdin.readline

dx=[-1,0,1,0]
dy=[0,1,0,-1]

n,m=map(int,input().split())
board=[list(map(int,input().rstrip())) for _ in range(n)]

q=deque()
q.append([0,0])
visited=[[0]*m for _ in range(n)]

while q:
  x,y=q.popleft()
  for i in range(4):
    xx,yy=x+dx[i],y+dy[i]
    if 0<=xx<n and 0<=yy<m and visited[xx][yy]==0 and board[xx][yy]==1:
      q.append([xx,yy])
      visited[xx][yy]=visited[x][y]+1

print(visited[n-1][m-1]+1)