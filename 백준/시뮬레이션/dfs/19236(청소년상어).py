import copy


def find_food(arr,x,y):
  position=[]
  dir=arr[x][y][1]
  for i in range(1,4):
    xx,yy=x+dx[dir],y+dy[dir]
    if 0<=xx<4 and 0<=yy<4 and 1<=arr[xx][yy][0]<=16:
      position.append([xx,yy])
    x,y=xx,yy
  return position

def find_fish(arr,index):
  for i in range(4):
    for j in range(4):
      if arr[i][j][0]==index:
        return (i,j)
  return None

def move_fish(arr,cx,cy):
  for i in range(1,17):
    position=find_fish(arr,i)
    if position==None:
      continue
    x,y=position[0],position[1]
    dir=arr[x][y][1]
    for i in range(8):
      xx=x+dx[dir]
      yy=y+dy[dir]
      if 0<=xx<4 and 0<=yy<4:
        if not (xx==cx and yy==cy):
          arr[xx][yy][0],arr[x][y][0]=arr[x][y][0],arr[xx][yy][0]
          arr[xx][yy][1],arr[x][y][1]=dir,arr[xx][yy][1]
          break
      dir=(dir+1)%8

def dfs(arr,x,y,total):
  global answer
  tmp=copy.deepcopy(arr)
  fish_number=tmp[x][y][0]
  tmp[x][y][0]=-1

  move_fish(tmp,x,y)

  eat_cnt=find_food(tmp,x,y)
  if len(eat_cnt)==0:
    answer=max(answer,total+fish_number)
    return 

  for nx,ny in eat_cnt:
    dfs(tmp,nx,ny,total+fish_number)
  
dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, -1, -1, -1, 0, 1, 1, 1]

data=[list(map(int,input().split())) for _ in range(4)]
board=[[0] * 4 for _ in range(4)]
# 배열을 [값,방향] 형태로 바꿈
for i in range(4):
  for j in range(4):
    board[i][j]=[data[i][2*j],data[i][j*2+1]-1]

answer=0

dfs(board,0,0,0)
print(answer)