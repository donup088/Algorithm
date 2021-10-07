t=int(input())

dp=[[0 for _ in range(31)] for _ in range(31)]
dp[0][0]=1

for num1 in range(1,31):
  dp[num1][0]=1
  for num2 in range(1,31):
    dp[num1][num2]=dp[num1-1][num2]+dp[num1-1][num2-1]

for _ in range(t):
  n,m=map(int,input().split())
  print(dp[m][n])