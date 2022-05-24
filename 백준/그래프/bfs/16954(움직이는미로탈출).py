from collections import deque

dx=[1,0,-1,0,1,1,-1,-1,0]
dy=[0,-1,0,1,-1,1,1,-1,0]

def bfs(cx,cy):
  global wall
  q=deque()
  q.append([cx,cy])
  
  while q:
    # 같은 레벨의 q를 모두 비우고 배열을 움직이고 나면 visted 배열 초기화
    visited=[[0]*8 for _ in range(8)]
    # 같은 레벨의 q를 모두 비우고 배열 움직이기
    for _ in range(len(q)):
      x,y=q.popleft()
      if (x,y) in wall:
        continue
      if x==0 and y==7:
        return 1
      for i in range(9):
        xx,yy=x+dx[i],y+dy[i]
        if 0<=xx<8 and 0<=yy<8 and visited[xx][yy]==0 and (xx,yy) not in wall:
          visited[xx][yy]=1
          q.append([xx,yy])
    
    # 배열이 하나씩 내려가는 것은 벽 좌표로 계싼
    next_wall=set()
    for x,y in wall:
      if x<7:
        next_wall.add((x+1,y))
    wall=next_wall
  return 0
    
      
board=[list(input().rstrip()) for _ in range(8)]
# set으로 벽 좌표 관리
wall=set()
for i in range(8):
  for j in range(8):
    if board[i][j]=='#':
      wall.add((i,j))
print(bfs(7,0))