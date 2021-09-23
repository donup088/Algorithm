n,m=map(int,input().split())
arr=[]
res=0
for _ in range(n):
  arr.append(list(map(int,input().split())))
for i in range(m):
  for j in range(i+1,m):
    for k in range(j+1,m):
      temp=0
      for l in range(n):
        temp+=max(arr[l][i],arr[l][j],arr[l][k])
      res=max(res,temp)

print(res)