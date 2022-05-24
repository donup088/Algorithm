from collections import deque

dx=[-1,0,1,0]
dy=[0,1,0,-1]
# N 세로 M 가로
N,M=map(int,input().split())
_map=[list(map(int,input().split())) for _ in range(N)]

def bfs(a,b):
  q=deque()
  q.append([a,b])
  visited[a][b]=1
  while q:
    x,y=q.popleft()
    for i in range(4):
      xx=x+dx[i]
      yy=y+dy[i]
      if 0<=xx<N and 0<=yy<M:
        if _map[xx][yy]!=0 and visited[xx][yy]==0:
          visited[xx][yy]=1
          q.append([xx,yy])
        elif _map[xx][yy]==0:
          count[x][y]+=1

day=0

while True:
  bfs_count=0
  visited = [[0]*M for _ in range(N)]
  count = [[0]*M for _ in range(N)]
  for i in range(N):
    for j in range(M):
      if _map[i][j]!=0 and visited[i][j]==0:
        bfs(i,j)
        bfs_count+=1
  for i in range(N):
    for j in range(M):
      if count[i][j]!=0:
        _map[i][j]-=count[i][j]
        if _map[i][j]<0:
          _map[i][j]=0
  
  if bfs_count>1:
    print(day)
    break
  if bfs_count==0:
    print(0)
    break

  day+=1