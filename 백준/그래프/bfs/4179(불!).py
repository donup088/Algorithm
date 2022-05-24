from collections import deque

def bfs(): 
  while fq:
    x,y=fq.popleft()
    for i in range(4):
      xx=x+dx[i]
      yy=y+dy[i]
      if 0<=xx<r and 0<=yy<c:
        if miro[xx][yy]!='#' and f_visited[xx][yy]==0:
          f_visited[xx][yy]=f_visited[x][y]+1
          fq.append((xx,yy))
          
  while jq:
    x,y=jq.popleft()
    for i in range(4):
      xx=x+dx[i]
      yy=y+dy[i]    
      if 0<=xx<r and 0<=yy<c:
        if j_visited[xx][yy]==0 and miro[xx][yy]!='#' :
          if f_visited[xx][yy]==0 or f_visited[xx][yy]>j_visited[x][y]+1:
            j_visited[xx][yy]=j_visited[x][y]+1
            jq.append((xx,yy))
      else:
        return j_visited[x][y]+1
  return 'IMPOSSIBLE'

dx=[-1,0,1,0]
dy=[0,1,0,-1]

#R 세로 C 가로
r,c=map(int,input().split())
miro=[list(input().rstrip()) for _ in range(r)]

f_visited=[[0]*c for _ in range(r)]
j_visited=[[0]*c for _ in range(r)]
fq=deque()
jq=deque()

for i in range(r):
  for j in range(c):
    if miro[i][j]=='F':
      fq.append((i,j))
    elif miro[i][j]=='J':
      jq.append((i,j))
print(bfs())