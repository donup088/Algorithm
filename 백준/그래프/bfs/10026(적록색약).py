import sys
input = sys.stdin.readline
from collections import deque

dx=[-1,0,1,0]
dy=[0,1,0,-1]

def bfs(cx,cy,color,board):
  global visited
  q=deque()
  q.append([cx,cy])
  visited[cx][cy]=1
  while q:
    x,y=q.popleft()
    for i in range(4):
      xx,yy=x+dx[i],y+dy[i]
      if 0<=xx<n and 0<=yy<n and visited[xx][yy]==0 and board[xx][yy]==color:
        visited[xx][yy]=1
        q.append([xx,yy])
  
n=int(input())
board=[list(input().rstrip()) for _ in range(n)]

g_board=[[0]*n for _ in range(n)]
visited=[[0]*n for _ in range(n)]
board_count=0
g_board_count=0

for i in range(n):
  for j in range(n):
    if board[i][j]=='R':
      g_board[i][j]='G'
    else:
      g_board[i][j]=board[i][j]

for i in range(n):
  for j in range(n):
    if visited[i][j]==0:
      bfs(i,j,board[i][j],board)
      board_count+=1

visited=[[0]*n for _ in range(n)]

for i in range(n):
  for j in range(n):
    if visited[i][j]==0:
      bfs(i,j,g_board[i][j],g_board)
      g_board_count+=1

print(board_count,g_board_count)
