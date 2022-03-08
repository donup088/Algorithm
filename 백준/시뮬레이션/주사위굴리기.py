import copy
dx=[0,0,-1,1]
dy=[1,-1,0,0]
n,m,x,y,k=map(int,input().split())
board=[]
dice=[0]*6
cx,cy=x,y

def move_dice(dir):
  tmp=copy.deepcopy(dice)
  # 동
  if dir==1:
    dice[2]=tmp[0]
    dice[0]=tmp[3]
    dice[5]=tmp[2]
    dice[3]=tmp[5]
  # 서
  elif dir==2:
    dice[0]=tmp[2]
    dice[2]=tmp[5]
    dice[5]=tmp[3]
    dice[3]=tmp[0]
  # 북
  elif dir==3:
    dice[0]=tmp[4]
    dice[4]=tmp[5]
    dice[5]=tmp[1]
    dice[1]=tmp[0]
  # 남
  elif dir==4:
    dice[4]=tmp[0]
    dice[5]=tmp[4]
    dice[1]=tmp[5]
    dice[0]=tmp[1]
  
def copy_dice(c_x,c_y):
  if board[c_x][c_y]==0:
    board[c_x][c_y]=dice[5]
  else:
    dice[5]=board[c_x][c_y]
    board[c_x][c_y]=0
    
for _ in range(n):
  board.append(list(map(int,input().split())))
dir=list(map(int,input().split()))

for d in dir:
  xx=cx+dx[d-1]
  yy=cy+dy[d-1]
  if 0<=xx<n and 0<=yy<m:
    move_dice(d)
    copy_dice(xx, yy)
    cx,cy=xx,yy
    print(dice[0])