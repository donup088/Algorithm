from collections import deque

N,L,R=map(int,input().split())
data=[]
dx=[-1,0,1,0]
dy=[0,1,0,-1]
for _ in range(N):
  data.append(list(map(int,input().split())))
res=0

def bfs(x,y):
  global total,flag
  union=deque()
  union.append((x,y))
  temp.append((x,y))
  while union:
    ux,uy=union.popleft()
    for i in range(4):
      xx=ux+dx[i]
      yy=uy+dy[i]
      if xx < 0 or xx >= N or yy < 0 or yy >= N:
        continue
      if visited[xx][yy]==0 and L<=abs(data[xx][yy]-data[ux][uy])<=R:
        visited[xx][yy]=1
        flag=1
        union.append((xx,yy))
        temp.append((xx,yy))
        total+=data[xx][yy]

while(True):
  flag=0
  visited=[[0]*N for _ in range(N)]

  for i in range(N):
    for j in range(N):
      if visited[i][j]==0:
        temp=deque()
        total=data[i][j]
        visited[i][j]=1
        bfs(i,j)
        if len(temp)>1:
          avg=total//len(temp)
          while temp:
            a,b=temp.popleft()
            data[a][b]=avg
  
  if flag==0:
    break
  res += 1
print(res)
