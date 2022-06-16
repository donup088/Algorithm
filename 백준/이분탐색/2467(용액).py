import sys

input = sys.stdin.readline

n=int(input())
data=list(map(int,input().split()))

left=0
right=n-1

_min=sys.maxsize
l=0
r=0

while left<right:
  _sum=data[left]+data[right]

  if abs(_sum)<_min:
    l=left
    r=right
    _min=abs(_sum)

  if _sum>0:
    right-=1
  elif _sum<0:
    left+=1
  else:
    break

print(data[l],data[r])