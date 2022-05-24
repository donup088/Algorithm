from collections import deque
dx=[1,0,-1,0]
dy=[0,1,0,-1]
# n 세로 m 가로
n,m,t=map(int,input().split())
_map=[list(map(int,input().split())) for _ in range(n)]

def bfs():
  q=deque()
  q.append([0,0])
  gram=1e9
  visited=[[0]*m for _ in range(n)]
  visited[0][0]=1
  while q:
    x,y=q.popleft()
    if x==n-1 and y==m-1:
      return min(visited[x][y]-1,gram)
    if _map[x][y]==2:
      gram=visited[x][y]-1+n-1-x+m-1-y
    for i in range(4):
      xx=x+dx[i]
      yy=y+dy[i]
      if 0<=xx<n and 0<=yy<m and visited[xx][yy]==0:
        if _map[xx][yy]!=1:
          visited[xx][yy]=visited[x][y]+1
          q.append((xx,yy))
  return gram

res=bfs()
if res>t:
  print('Fail')
else:
  print(res)