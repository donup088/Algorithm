n,m=map(int,input().split())
data=list(map(int,input().split()))

left=0
right=1
answer=0
while right<=n and left<=right:
  tmp=sum(data[left:right])
  if tmp==m:
    answer+=1
    right+=1
  elif tmp>m:
    left+=1
  else:
    right+=1
  
print(answer)