n=int(input())
p=[]
t=[]
dp=[0]*(n+1)

for i in range(n):
  a,b=map(int,input().split())
  t.append(a)
  p.append(b)
k=0
for i in range(n):
  k=max(k,dp[i])
  if i+t[i]>n:
    continue
  dp[i+t[i]]=max(k+p[i],dp[i+t[i]])

print(max(dp))