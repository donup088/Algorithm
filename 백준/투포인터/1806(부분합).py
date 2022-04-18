n,s=map(int,input().split())
data=list(map(int,input().split()))

sum=[0]*(n+1)
for i in range(1,n+1):
  sum[i]=sum[i-1]+data[i-1]

answer=1e9
left=0
right=1
while left<n:
  if sum[right]-sum[left]>=s:
    if right-left<answer:
      answer=right-left
    left+=1
  else:
    if right<n:
      right+=1
    else:
      left+=1

if answer!=1e9:
  print(answer)
else:
  print(0)