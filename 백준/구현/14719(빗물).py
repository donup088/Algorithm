H,W=map(int,input().split())
data=list(map(int,input().split()))
res=0
temp=data[0]
for i in range(len(data)):
  max_left=max(data[:i+1])
  max_right=max(data[i:])
  min_data=min(max_left,max_right)
  res+=min_data-data[i]
print(res)