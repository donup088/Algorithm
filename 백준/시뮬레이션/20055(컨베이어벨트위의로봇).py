from collections import deque

n,k=map(int,input().split())
arr=deque(map(int,input().split()))
bot=deque([0]*(n*2))

res=1
while True:
  arr.rotate(1)
  bot.rotate(1)
  bot[n-1]=0
  for i in range(n-2,-1,-1):
    if(bot[i]!=0 and bot[i+1]==0 and arr[i+1]>=1):
      arr[i+1]-=1
      bot[i+1]=bot[i]
      bot[i]=0
    bot[n-1]=0
  if(bot[0]==0 and arr[0]>0):
    arr[0]-=1
    bot[0]=1
  if arr.count(0)>=k:
    print(res)
    break
  res+=1