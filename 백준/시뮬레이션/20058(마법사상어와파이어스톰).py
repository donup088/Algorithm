from collections import deque

dx=[-1,0,1,0]
dy=[0,1,0,-1]

N,Q=map(int,input().split())
ices=[list(map(int,input().split())) for _ in range(2**N)]
L=list(map(int,input().split()))

n=2**N
for l in L:
  rotate_arr=[[0]*n for _ in range(n)]
  for i in range(0,n,2**l):
    for j in range(0,n,2**l):
      for i2 in range(2**l):
        for j2 in range(2**l):
          rotate_arr[i+j2][j+2**l-i2-1]=ices[i+i2][j+j2]

  ices=[[0]*n for _ in range(n)]
  
  for i in range(n):
    for j in range(n):
      cnt=0
      for k in range(4):
        xx=i+dx[k]
        yy=j+dy[k]
        if 0<=xx<n and 0<=yy<n and rotate_arr[xx][yy]!=0:
          cnt+=1
      if rotate_arr[i][j]>0:
        if cnt<3:
          ices[i][j]=rotate_arr[i][j]-1
        else:
          ices[i][j]=rotate_arr[i][j]
total=0
_max=0
for i in range(n):
  for j in range(n):
    if ices[i][j]==0:
      continue
    cnt=0
    q=deque()
    q.append([i,j])
    total+=ices[i][j]
    ices[i][j]=0
    while q:
      x,y=q.popleft()
      cnt+=1
      for k in range(4):
        xx=x+dx[k]
        yy=y+dy[k]
        if 0<=xx<n and 0<=yy<n and ices[xx][yy]!=0:
          q.append([xx,yy])
          total+=ices[xx][yy]
          ices[xx][yy]=0
    _max=max(_max,cnt)
print(total)
print(_max)