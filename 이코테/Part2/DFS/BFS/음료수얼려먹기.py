def DFS(x,y):
  if x >= n or x<=-1 or y >= m or y<=-1:
    return 
  if arr[x][y]==0:
    arr[x][y]=1
    DFS(x+1,y)
    DFS(x-1,y)
    DFS(x,y+1)
    DFS(x,y-1)
    


n,m=map(int,input().split())
res=0
arr=[]
for _ in range(n):
  arr.append(list(map(int,input())))

for i in range(n):
  for j in range(m):
    if arr[i][j]==0:
      DFS(i,j)
      res+=1
print(res)

