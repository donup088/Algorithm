import sys

input = sys.stdin.readline

n=int(input())
data=[]
for _ in range(n):
  a,b=map(int,input().split())
  data.append([a,b])

data.sort()

dp=[1]*n
for i in range(n):
  for j in range(i):
    if data[i][1]>data[j][1]:
      dp[i]=max(dp[i],dp[j]+1)

print(n-max(dp))