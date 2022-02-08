from collections import deque
dx=[-1,0,1,0]
dy=[0,1,0,-1]
# M 가로 N 세로
def bfs():
  q=deque()
  q.append([0,0,1])
  dist=[[[0]*2 for _ in range(m)] for _ in range(n)]
  dist[0][0][1]=1

  while q:
    x,y,w=q.popleft()
    if x==n-1 and y==m-1:
      return dist[x][y][w]
    for i in range(4):
      xx=x+dx[i]
      yy=y+dy[i]
      if 0<=xx<n and 0<=yy<m:
        if MAP[xx][yy]==1 and w==1:
          dist[xx][yy][0]=dist[x][y][1]+1
          q.append([xx,yy,0])
        elif MAP[xx][yy]==0 and dist[xx][yy][w]==0:
          dist[xx][yy][w]=dist[x][y][w]+1
          q.append([xx,yy,w])
  return -1


n,m=map(int,input().split())
MAP=[list(map(int,input().rstrip())) for _ in range(n)]
print(bfs())