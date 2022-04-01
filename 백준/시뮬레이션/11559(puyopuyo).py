from collections import deque

dx=[-1,0,1,0]
dy=[0,1,0,-1]
board=[list(input().rstrip()) for _ in range(12)]
answer=0

def bfs(cx,cy,color):
  visited=[[0]*6 for _ in range(12)]
  res=[]
  q=deque()
  q.append([cx,cy])
  visited[cx][cy]=1
  res.append([cx,cy])
  while q:
    x,y=q.popleft()
    for i in range(4):
      xx=x+dx[i]
      yy=y+dy[i]
      if 0<=xx<12 and 0<=yy<6 and visited[xx][yy]==0:
        visited[xx][yy]=1
        if board[xx][yy]==color:
          res.append([xx,yy])
          q.append([xx,yy])
  if len(res)>=4:
    return res
  else:
    return []

def down(arr,bomb_list):
  for b in bomb_list:
    for i in range(b[0],0,-1):
      arr[i][b[1]]=arr[i-1][b[1]]
  arr[0][b[1]]='.'
  return arr
  
bomb=[]

while True:
  for i in range(12):
    for j in range(6):
      if board[i][j]!='.':  
          tmp=bfs(i,j,board[i][j])
          if len(tmp)>0:
            for t in tmp:
              if t not in bomb:
                bomb.append(t)
  # 터지는 블록이 없다면 종료
  if len(bomb)==0:
    break
  board=down(board,bomb)
  answer+=1
  bomb=[]
print(answer)