n,k=map(int,input().split())
data=[]
for i in range(n):
  data.append(int(input()))

dp=[10001]*(k+1)
dp[0]=0

for n in data:
  for i in range(n,k+1):
    dp[i]=min(dp[i],dp[i-n]+1)

if dp[k]==10001:
  print(-1)
else:
  print(dp[k])