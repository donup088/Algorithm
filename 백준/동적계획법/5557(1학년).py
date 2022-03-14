n=int(input())
arr=list(map(int,input().split()))
dp=[]
for i in range(n-1):
  dp.append([0 for _ in range(21)])
#dp[i][j]=i번째 숫자까지 연산을 진행했을 때 j값을 나타낼 수 있는 경우의수
dp[0][arr[0]]=1

for i in range(1,n-1):
  for j in range(21):
      if 0<=j+arr[i]<=20:
        dp[i][j+arr[i]]+=dp[i-1][j]
      if 0<=j-arr[i]<=20:
        dp[i][j-arr[i]]+=dp[i-1][j]

print(dp[n-2][arr[n-1]])