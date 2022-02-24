n=int(input())
numbers=list(map(int,input().split()))
dp=[numbers[0]]
for i in range(n-1):
  dp.append(max(dp[i]+numbers[i+1],numbers[i+1]))
print(max(dp))