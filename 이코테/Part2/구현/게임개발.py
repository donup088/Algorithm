def turn_left():
  global d
  d-=1
  if d==-1:
    d=3

n,m=map(int,input().split())
x,y,d=map(int,input().split())
arr=[]
ch=[[0] * m for _ in range(n)]
for _ in range(n):
  arr.append(list(map(int,input().split())))

res=0
dx=[-1,0,1,0]
dy=[0,1,0,-1]
turn_count=0
while True:
    turn_left()
    xx=x+dx[d]
    yy=y+dy[d]
    if arr[xx][yy]==0 and ch[xx][yy]==0:
      ch[xx][yy]=1
      x=xx
      y=yy
      res+=1
      turn_count=0
    else:
      turn_count+=1
    if turn_count==4:
      xx=x-dx[d]
      yy=y-dy[d]
      if arr[xx][yy]==0:
        x=xx
        y=yy
      else:
        break
      turn_count=0
print(res)