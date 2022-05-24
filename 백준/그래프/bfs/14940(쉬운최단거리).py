from collections import deque
dx=[1,0,-1,0]
dy=[0,1,0,-1]

#n 세로 m 가로
n,m=map(int,input().split())
_map=[list(map(int,input().split())) for _ in range(n)]
cx,cy=0,0
for i in range(n):
  for j in range(m):
    if _map[i][j]==2:
      cx,cy=i,j

visited=[[-1]*m for _ in range(n)]
q=deque()
q.append([cx,cy])
visited[cx][cy]=0
while q:
  x,y=q.popleft()
  for k in range(4):
    xx=x+dx[k]
    yy=y+dy[k]
    if 0<=xx<n and 0<=yy<m and visited[xx][yy]==-1:
      if _map[xx][yy]==1:
        q.append([xx,yy])
        visited[xx][yy]=visited[x][y]+1
      
for i in range(n):
  for j in range(m):
    if _map[i][j]==0:
      print(0, end=' ')
    else:
      print(visited[i][j],end=' ')
  print()