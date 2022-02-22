n=int(input())
stone=[]
dp=[1e9]*n
dp[0]=0

for i in range(n-1):
  a,b=map(int,input().split())
  stone.append([a,b])
  if i+1<n: 
    dp[i+1]=min(dp[i+1],dp[i]+a)
  if i+2<n:
    dp[i+2]=min(dp[i+2],dp[i]+b)

k=int(int(input()))
res=dp[-1]
for i in range(3,n):
  tmp=dp[i-3]+k
  dp1,dp2=1e9,1e9
  for j in range(i,n-1):
    if i+1<=n:
      dp1=min(dp1,tmp+stone[j][0])
    if i+2<=n:
      dp2=min(dp2,tmp+stone[j][1])
      tmp,dp1,dp2=dp1,dp2,1e9
  res=min(res,tmp)
print(res)

# dfs 풀이
# n=int(input())
# stone=[[0,0]]

# for i in range(n-1):
#   a,b=map(int,input().split())
#   stone.append([a,b])
# k=int(input())
# res=1e9 

# def dfs(idx,used,val):
#   global res
#   if idx==n:
#     res=min(res,val)
#     return 
#   if idx+1<=n:
#     dfs(idx+1,used,val+stone[idx][0])
#   if idx+2<=n:
#     dfs(idx+2,used,val+stone[idx][1])
#   if idx+3<=n and not used:
#     dfs(idx+3,True,val+k)

# dfs(1,0,0)
# print(res)