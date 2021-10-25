A=[]
move=[]
cloud=[]
res=0
dx=[0,-1,-1,-1,0,1,1,1]
dy=[-1,-1,0,1,1,1,0,-1]
N,M=map(int,input().split())
for _ in range(N):
  A.append(list(map(int,input().split())))
for _ in range(M):
  move.append(list(map(int,input().split())))

cloud.append((N-2,0))
cloud.append((N-2,1))
cloud.append((N-1,0))
cloud.append((N-1,1))

for i in range(M):
  d,s=move[i][0]-1,move[i][1]
  visited = [[0]*N for _ in range(N)]
  new_cloud=[]
  for j in range(len(cloud)):
    xx=(N+cloud[j][0]+dx[d]*s)%N
    yy=(N+cloud[j][1]+dy[d]*s)%N
    new_cloud.append((xx,yy))
    visited[xx][yy]=1
  for k in range(len(new_cloud)):
    A[new_cloud[k][0]][new_cloud[k][1]]+=1

  save=[]

  for j in range(len(new_cloud)):
    cnt=0
    for k in range(1,8,2):
      xx=new_cloud[j][0]+dx[k]
      yy=new_cloud[j][1]+dy[k]
      if xx<0 or xx>=N:
        continue
      if yy<0 or yy>=N:
        continue
      if A[xx][yy]>0:
        cnt+=1
    save.append(cnt)
  
  for j in range(len(new_cloud)):
    A[new_cloud[j][0]][new_cloud[j][1]]+=save[j]
  
  cloud=[]
  for j in range(N):
    for k in range(N):
      if visited[j][k]==0 and A[j][k]>=2:
        A[j][k]-=2 
        cloud.append((j,k))

for i in range(N):
  for j in range(N):
    if A[i][j]>0:
      res+=A[i][j]

print(res)