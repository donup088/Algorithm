from collections import deque

def passenger_bfs(s_x,s_y):
  q=deque()
  q.append([s_x,s_y])
  visited=[[0]*n for _ in range(n)]
  visited[s_x][s_y]=1
  distance=[[1e9]*n for _ in range(n)]
  distance[s_x][s_y]=0
  while q:
    x,y=q.popleft()
    for i in range(4):
      xx=x+dx[i]
      yy=y+dy[i]
      if 0<=xx<n and 0<=yy<n and visited[xx][yy]==0:
        if board[xx][yy]!=1:
          visited[xx][yy]=1
          distance[xx][yy]=distance[x][y]+1
          q.append([xx,yy])
  return distance

def taxi_bfs(s_x,s_y,e_x,e_y):
  q=deque()
  q.append([s_x,s_y])
  visited=[[0]*n for _ in range(n)]
  visited[s_x][s_y]=1
  distance=[[0]*n for _ in range(n)]
  while q:
    x,y=q.popleft()
    if x==e_x and y==e_y:
      return distance[x][y]
    for i in range(4):
      xx=x+dx[i]
      yy=y+dy[i]
      if 0<=xx<n and 0<=yy<n and visited[xx][yy]==0:
        if board[xx][yy]!=1:
          visited[xx][yy]=1
          distance[xx][yy]=distance[x][y]+1
          q.append([xx,yy])
  return -1    

dx=[-1,0,1,0]
dy=[0,1,0,-1]
  
n,m,o=map(int,input().split())
board=[list(map(int,input().split())) for _ in range(n)]

r,c=map(int,input().split())
passenger=[]
for _ in range(m):
  _a,_b,_c,_d=map(int,input().split())
  passenger.append([[_a-1,_b-1],[_c-1,_d-1]])
start_x,start_y=r-1,c-1

while m>0:
  cost=[]
  # 최단 경로에 위치해 있는 손님 찾기  
  # 현재위치에서 bfs를 통해 전체 위치 최단거리를 찾고 distance 배열을 return 
  dis=passenger_bfs(start_x,start_y)
  for i in range(len(passenger)):
    cost.append((dis[passenger[i][0][0]][passenger[i][0][1]],passenger[i][0][0],passenger[i][0][1],passenger[i][1][0],passenger[i][1][1],i))
  # 벽에 막혀서 갈 수 없음
  if len(cost)!=len(passenger):
    print(-1)
    break
  # 제일 가까운 손님에게 도착
  cost=sorted(cost, key=lambda s: (s[0],s[1],s[2]))
  o=o-cost[0][0]
  # 손님에게 도착할 수 있는 지 연료 체크
  if o<0:
    print(-1)
    break
  # 손님을 태우고 목적지로 이동
  des_dis=taxi_bfs(cost[0][1],cost[0][2],cost[0][3],cost[0][4])
  # 목적지로 이동할 수 없는 경우
  if des_dis==-1:
    print(-1)
    break
  # 목적지로 이동할 수 있는 지 연료 체크
  o=o-des_dis
  if o<0:
    print(-1)
    break
  # 목적지 도착 후 연료 보충
  o+=des_dis*2
  m-=1
  # 태웠던 손님 제거
  passenger.pop(cost[0][5])
  start_x,start_y=cost[0][3],cost[0][4]
  
if not passenger:
  print(o)    