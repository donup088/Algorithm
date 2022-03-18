#n 세로 m 가로
n,m=map(int,input().split())
arr=[list(map(int,input().split())) for _ in range(n)]

dp=[[[1e9]*3 for _ in range(m)] for _ in range(n)]

answer=1e9

for i in range(n):
  if i==0:
    for j in range(m):
      for d in range(3):
        dp[i][j][d]=arr[i][j]
  else:
    for j in range(m):
      if j==0:
        dp[i][j][0]=min(dp[i-1][j+1][1],dp[i-1][j+1][2])+arr[i][j]
        dp[i][j][1]=dp[i-1][j][0]+arr[i][j]
      elif j==m-1:
        dp[i][j][1]=dp[i-1][j][2]+arr[i][j]
        dp[i][j][2]=min(dp[i-1][j-1][1],dp[i-1][j-1][0])+arr[i][j]
      else:
        dp[i][j][0]=min(dp[i-1][j+1][1],dp[i-1][j+1][2])+arr[i][j]
        dp[i][j][1]=min(dp[i-1][j][0],dp[i-1][j][2])+arr[i][j]
        dp[i][j][2]=min(dp[i-1][j-1][0],dp[i-1][j-1][1])+arr[i][j]

for i in range(m):
    answer = min(min(dp[n-1][i]), answer)
print(answer)