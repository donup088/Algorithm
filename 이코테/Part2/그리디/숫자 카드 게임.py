n, m =map(int,input().split())

res=-2147000000
for i in range(n):
  data=list(map(int,input().split()))
  m=min(data)
  res=max(m,res)
print(res)