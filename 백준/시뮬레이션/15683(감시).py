import copy

dx=[1,-1,0,0]
dy=[0,0,1,-1]
direction = [[], [[0], [1], [2], [3]], [[0, 1], [2, 3]], [[0, 2], [2, 1], [1, 3], [3, 0]],[[3, 0, 2], [1, 3, 0], [0, 2, 1], [2, 1, 3]], [[0, 1, 2, 3]]]

def fill(tmp,d,x,y):
  for i in d:
    xx,yy=x,y
    while True:
      xx+=dx[i]
      yy+=dy[i]
      if xx<0 or yy<0 or xx>=N or yy>=M or tmp[xx][yy]==6:
        break
      elif tmp[xx][yy]==0:
        tmp[xx][yy]='#'

def dfs(idx,arr):
  global ans
  if idx==len(cctv):
    cnt=0
    for i in range(N):
      cnt+=arr[i].count(0)
    ans=min(ans,cnt)
    return 
  x,y,num=cctv[idx]
  tmp=copy.deepcopy(arr)
  for d in direction[num]: 
    fill(tmp,d,x,y)
    dfs(idx+1,tmp)
    tmp=copy.deepcopy(arr)


ans=1e9
N,M=map(int,input().split())
office=[]
cctv=[]
for _ in range(N):
  office.append(list(map(int,input().split())))
for i in range(N):
  for j in range(M):
    if 1<=office[i][j]<=5:
      cctv.append((i,j,office[i][j]))

dfs(0,office)
print(ans)
  