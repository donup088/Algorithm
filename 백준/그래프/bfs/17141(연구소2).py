from itertools import combinations
from collections import deque
import copy

dx=[-1,0,1,0]
dy=[0,1,0,-1]

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

def bfs(start):
  distance=[[-1]*n for _ in range(n)]
  q=deque()
  max_dis=0
  tmp=copy.deepcopy(board)
  for v in virus:
    if v not in start:
      tmp[v[0]][v[1]]=0
  for s in start:
    q.append([s[0],s[1]])
    distance[s[0]][s[1]]=0
  while q:
    x,y=q.popleft()
    for i in range(4):
      xx,yy=x+dx[i],y+dy[i]
      if 0<=xx<n and 0<=yy<n and distance[xx][yy]==-1 and tmp[xx][yy]!=1:
        q.append([xx,yy])
        distance[xx][yy]=distance[x][y]+1
        if tmp[xx][yy]==0:
          max_dis=max(max_dis,distance[xx][yy])
  if check_spread(distance,wall):
    answer.append(max_dis)

n,m=map(int,input().split())
virus=[]
board=[]
answer=[]
wall=0
for _ in range(n):
  board.append(list(map(int,input().split())))

for i in range(n):
  for j in range(n):
    if board[i][j]==1:
      wall+=1
    if board[i][j]==2:
      virus.append([i,j])
