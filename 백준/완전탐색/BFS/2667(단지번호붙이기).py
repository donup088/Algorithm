from collections import deque

dx=[-1,0,1,0]
dy=[0,1,0,-1]

n=int(input())
board=[list(map(int,input().rstrip())) for _ in range(n)]
house=[]

def bfs(cx,cy): 
  cnt=0
  while q:
    x,y=q.popleft()
    for i in range(4):
      xx=x+dx[i]
      yy=y+dy[i]
      if 0<=xx<n and 0<=yy<n:
        if board[xx][yy]==1:
          q.append([xx,yy])
          board[xx][yy]=0
    cnt+=1
  return cnt

for i in range(n):
  for j in range(n):
    if board[i][j]==1:
      q=deque()
      q.append([i,j])
      board[i][j]=0
      house.append(bfs(i,j))

print(len(house))
house.sort()
for h in house:
  print(h)