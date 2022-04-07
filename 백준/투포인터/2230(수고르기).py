import sys

n,m=map(int,input().split())
data=[]
for _ in range(n):
  data.append(int(input()))

left=0
right=1
answer=sys.maxsize
data.sort()
while left<n and right<n:
  diff=data[right]-data[left]
  if diff==m:
    print(diff)
    exit(0)
  if diff<m:
    right+=1
    continue
  left+=1
  answer=min(answer,diff)
print(answer)