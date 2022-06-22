import sys

input = sys.stdin.readline

n=int(input())
data=list(map(int,input().split()))

dp=[1e9]*n
dp[0]=0
for i in range(n-1):
  for j in range(1,data[i]+1):
    if i+j<n:
      if dp[i+j]>dp[i]+1:
        dp[i+j]=dp[i]+1

if dp[n-1]!=1e9:
  print(dp[n-1])
else:
  print(-1)