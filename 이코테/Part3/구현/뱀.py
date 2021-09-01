import sys
sys.stdin=open("input.txt","r")

def getDirection(d):
  if d == 'D':
    return (direction+1)%4
  if d == 'L':
    return (direction-1)%4

n=int(input())#보드크기
k=int(input())#사과개수
m=[[0]*(n+1) for _ in range(n+1)]
for _ in range(k):
  x,y=map(int,input().split())
  m[x][y]=1
l=int(input())
d=[]
for _ in range(l):
  a,b=input().split()
  d.append((int(a),b))

dx=[0,1,0,-1]
dy=[1,0,-1,0]

x=1 #현재위치
y=1 #현재위치
m[x][y]=2#뱀 위치 2로 표현
time=0
index=0
tail=[(x,y)]
direction=0

while True:
  xx=x+dx[direction]
  yy=y+dy[direction]

  if 1<=xx<=n and 1<=yy<=n and m[xx][yy]!=2:
    if m[xx][yy]==1:
      m[xx][yy]=2
      tail.append((xx,yy))
    if m[xx][yy]==0:
      m[xx][yy]=2
      tail.append((xx,yy))
      tx,ty=tail.pop(0)
      m[tx][ty]=0
  else:
    time+=1
    break
  x, y = xx,yy
  time+=1
  if index<l and time==d[index][0]:
    direction=getDirection(d[index][1])
    index+=1

print(time)    


  
  

