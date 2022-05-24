from itertools import combinations

dx=[-1,0,1,0]
dy=[0,1,0,-1]

n=int(input())
arr=[]
price=[]
res=1e9
for _ in range(n):
  arr.append(list(map(int,input().split())))

for i in range(1, n-1):
  for j in range(1, n-1):
    price.append((i,j))

for flower in combinations(price,3):
  temp=0
  flag=0
  visited=[[0]*n for _ in range(n)]
  for f in flower:
    if visited[f[0]][f[1]]==0:
      visited[f[0]][f[1]]=1
      temp+=arr[f[0]][f[1]]
    else:
      flag=1
      break
    for i in range(4):
      xx=f[0]+dx[i]
      yy=f[1]+dy[i]
      if visited[xx][yy]==0:
        visited[xx][yy]=1
        temp+=arr[xx][yy]
      else:
        flag=1
        break
  if not flag:
    res=min(res,temp)

print(res)


    