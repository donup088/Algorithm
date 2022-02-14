n=int(input())
data=[]
for _ in range(n):
  data.append(int(input()))
dp=[0]
dp.append(data[0])
if n>1:
  dp.append(data[1]+data[0])

for i in range(3,n+1):
  dp.append(max(dp[i-3]+data[i-1]+data[i-2],dp[i-2]+data[i-1]))
print(dp[n])