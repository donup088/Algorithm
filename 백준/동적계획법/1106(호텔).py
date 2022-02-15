c,n=map(int,input().split())
cost_list=[]
for i in range(n):
  a,b=map(int,input().split())
  cost_list.append([a,b])

dp=[0]+[1e9]*(c+100)

for cost,customer in cost_list:
  for cur_customer in range(customer,c+101):
    dp[cur_customer]=min(dp[cur_customer],dp[cur_customer-customer]+cost)
    
print(min(dp[c:c+101]))