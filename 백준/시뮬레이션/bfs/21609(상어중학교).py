from collections import deque

dx=[1,0,-1,0]
dy=[0,1,0,-1]

def bfs(cx,cy):
  q=deque()
  q.append([cx,cy])
  visited[cx][cy]=1
  rainbow=[]
  blocks=[]
  blocks.append([cx,cy])
  while q:
    x,y=q.popleft()
    for i in range(4):
      xx,yy=x+dx[i],y+dy[i]
      if 0<=xx<n and 0<=yy<n and visited[xx][yy]==0:
        if board[xx][yy]==board[cx][cy] or board[xx][yy]==0:
          if board[xx][yy]==0:
            rainbow.append([xx,yy])
          blocks.append([xx,yy])
          q.append([xx,yy])
          visited[xx][yy]=1
  for r in rainbow:
    visited[r[0]][r[1]]=0

  return len(blocks),len(rainbow),blocks

def remove_block(blocks):
  for b in blocks:
    board[b[0]][b[1]]=-2

def gravity():
  for i in range(n-2,-1,-1):
    for j in range(n):
      if board[i][j]>-1:
        r=i
        while True:
          if 0<=r+1<n and board[r+1][j]==-2:
            board[r+1][j]=board[r][j]
            board[r][j]=-2
            r+=1
          else:
            break

def left_rotate_90():
  tmp = [[0]*n for _ in range(n)]
  for i in range(n):
    for j in range(n):
      tmp[n-1-j][i] = board[i][j]
  return tmp

n,m=map(int,input().split())
board=[list(map(int,input().split())) for _ in range(n)]
score=0
cnt=1
while True:
  visited=[[0]*n for _ in range(n)]
  block_infos=[]
  for i in range(n):
    for j in range(n):
      if visited[i][j]==0 and board[i][j]>0:
        block_info=bfs(i,j)
        if block_info[0]>=2:
          block_infos.append(block_info)
          
  block_infos.sort(reverse=True)

  if len(block_infos)==0:
    break
    
  remove_block(block_infos[0][2])
  score+=block_infos[0][0]**2
  gravity()
  board=left_rotate_90()
  gravity()

print(score)
    