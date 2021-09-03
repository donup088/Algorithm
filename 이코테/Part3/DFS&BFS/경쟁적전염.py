import sys
from collections import deque
sys.stdin=open("input.txt","r")

dx=[-1,0,1,0]
dy=[0,1,0,-1]

n,k=map(int,input().split())
data=[]
for _ in range(n):
  data.append(list(map(int,input().split())))
s,rx,ry=map(int,input().split())

location=[0]* (k+1)

for i in range(n):
  for j in range(n):
    for m in range(1,k+1):
      if data[i][j]==m:
        location[m]=(i,j,0)
q=deque(location[1:])

while q:
  x,y,t=q.popleft()
  if t==s:
    break
  for i in range(4):
    xx=x+dx[i]
    yy=y+dy[i]
    if 0<=xx<n and 0<=yy<n and data[xx][yy]==0:
      data[xx][yy]=data[x][y]
      q.append((xx,yy,t+1))

print(data[rx-1][ry-1])