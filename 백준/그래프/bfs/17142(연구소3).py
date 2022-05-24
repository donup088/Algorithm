from collections import deque
from itertools import combinations
from copy import deepcopy

def check_spread(arr,wall):
  cnt=0
  for i in range(len(arr)):
    for j in range(len(arr)):
      if arr[i][j]==-1:
        cnt+=1
  if cnt==wall:
    return True
  else:
    return False
        
def bfs(virus_start):
  _max=0
  distance=[[-1] * n for _ in range(n)]
  q=deque()
  for vs in virus_start:
    q.append(vs)
    distance[vs[0]][vs[1]]=0
  while q:
    x,y=q.popleft()
    for i in range(4):
      xx=x+dx[i]
      yy=y+dy[i]
      if 0<=xx<n and 0<=yy<n and board[xx][yy]!=1 and distance[xx][yy]==-1:
        distance[xx][yy]=distance[x][y]+1
        if board[xx][yy]==0:
          _max=max(_max,distance[xx][yy])
        q.append([xx,yy])
  tmp=deepcopy(distance)

  if check_spread(tmp,wall):
    answer.append(_max)
  
dx=[-1,0,1,0]
dy=[0,1,0,-1]

n,m=map(int,input().split())
board=[list(map(int,input().split())) for _ in range(n)]
virus=[]
answer=[]
wall=0
for i in range(n):
  for j in range(n):
    if board[i][j]==2:
      virus.append([i,j])
    if board[i][j]==1:
      wall+=1
for v in combinations(virus,m):
  bfs(v)
  
if len(answer)==0:
  print(-1)
else:
  print(min(answer))