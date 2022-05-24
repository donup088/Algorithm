import sys
from collections import deque

input = sys.stdin.readline

dx=[-1,0,1,0]
dy=[0,1,0,-1]

#r행c열
r,c=map(int,input().split())

board=[list(input().rstrip()) for _ in range(r)]

def bfs(waters,cx,cy):
  ## 물이 가는 경로 비용 계산
  cost=0
  wq=deque()
  water_visited=[[0]*c for _ in range(r)]
  for w in waters:
    wq.append([w[0],w[1]])
  while wq:
    wx,wy=wq.popleft()
    for i in range(4):
      next_wx,next_wy=wx+dx[i],wy+dy[i]
      if 0<=next_wx<r and 0<=next_wy<c:
        if board[next_wx][next_wy]=='D':
          water_visited[next_wx][next_wy]=1e9
        if water_visited[next_wx][next_wy]==0 and board[next_wx][next_wy]!='D' and board[next_wx][next_wy]!='S' and board[next_wx][next_wy]!='X':
          water_visited[next_wx][next_wy]=water_visited[wx][wy]+1
          wq.append([next_wx,next_wy])
          
  ## 고슴도치가 가는 경로
  gq=deque()
  gq.append([cx,cy])  
  go_visited=[[0]*c for _ in range(r)]
  
  while gq:
    gx,gy=gq.popleft()
    if board[gx][gy]=='D':
      return go_visited[gx][gy]
    for i in range(4):
      next_gx,next_gy=gx+dx[i],gy+dy[i]
      if 0<=next_gx<r and 0<=next_gy<c:
        if (go_visited[gx][gy]+1<water_visited[next_gx][next_gy] or water_visited[next_gx][next_gy]==0) and board[next_gx][next_gy]!='X' and go_visited[next_gx][next_gy]==0:
          gq.append([next_gx,next_gy])
          go_visited[next_gx][next_gy]=go_visited[gx][gy]+1
  
  return cost
  
water=[]
cx,cy=0,0

for i in range(r):
  for j in range(c):
    if board[i][j]=='*':
      water.append([i,j])
    elif board[i][j]=='S':
      cx,cy=i,j      
    
cost=bfs(water,cx,cy)
if cost==0:
  print('KAKTUS')
else:
  print(cost)