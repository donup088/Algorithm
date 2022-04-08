def binary_search(arr,k):
  diff=1e9
  left=0
  right=len(arr)-1
  count=1
  while left<right:
    hap=data[left]+data[right]
    tmp_diff=abs(k-hap)
    if hap<=k:
      left+=1
    else:
      right-=1
    if diff==tmp_diff:
      count+=1
    else:
      if tmp_diff<diff:
        diff=tmp_diff
        count=1
  return count
  
t=int(input())
for _ in range(t):
  n,k=map(int,input().split())
  data=list(map(int,input().split()))
  data.sort()
  print(binary_search(data,k))