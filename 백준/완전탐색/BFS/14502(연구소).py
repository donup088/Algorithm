from collections import deque
from itertools import combinations
import copy
dx=[1,0,-1,0]
dy=[0,1,0,-1]

def bfs(arr):
  safe_zone=0
  q=deque()
  visited=[[0]*M for _ in range(N)]
  for i in range(N):
    for j in range(M):
      if arr[i][j]==2:
        q.append([i,j])
        visited[i][j]=1
        while q:
          x,y=q.popleft()
          for k in range(4):
            xx=x+dx[k]
            yy=y+dy[k]
            if 0<=xx<N and 0<=yy<M and visited[xx][yy]==0:
              if arr[xx][yy]==0:
                arr[xx][yy]=2
                visited[xx][yy]=1
                q.append([xx,yy])

  for i in range(N):
    for j in range(M):
      if arr[i][j]==0:
        safe_zone+=1
  return safe_zone
#N 세로 M 가로
N,M=map(int,input().split())

_map=[list(map(int,input().split())) for _ in range(N)]

space=[]
res=[]

for i in range(N):
  for j in range(M):
    if _map[i][j]==0:
      space.append([i,j])

combs=combinations(space,3)

for comb in combs:
  tmp=copy.deepcopy(_map)
  for x,y in comb:
    tmp[x][y]=1
  res.append(bfs(tmp))
print(max(res))  