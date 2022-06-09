import sys
sys.stdin = open("input.txt", "r")

input = sys.stdin.readline

n=int(input())
data=list(map(int,input().split()))
dp=[0]*n
dp[0]=data[0]
for i in range(1,n):
  for j in range(i):
    if data[j]<data[i]:
      dp[i]=max(dp[i],dp[j]+data[i])
    else:
      dp[i]=max(dp[i],data[i])

print(max(dp))