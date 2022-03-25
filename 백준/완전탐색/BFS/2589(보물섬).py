from collections import deque

dx=[-1,0,1,0]
dy=[0,1,0,-1]

c,r=map(int,input().split())
board=[]
answer=0
for _ in range(c):
  board.append(list(input().rstrip()))

def bfs(cx,cy):
  q=deque()
  q.append([cx,cy])
  visited=[[0]*r for _ in range(c)]
  visited[cx][cy]=1

  while q:
    x,y=q.popleft()
    for i in range(4):
      xx=x+dx[i]
      yy=y+dy[i]
      if 0<=xx<c and 0<=yy<r and visited[xx][yy]==0:
        if board[xx][yy]=='L':
          q.append([xx,yy])
          visited[xx][yy]=visited[x][y]+1
  return max(map(max,visited))

for i in range(c):
  for j in range(r):
    if board[i][j]=='L':
      answer=max(answer,bfs(i,j))

print(answer-1)