import sys

input = sys.stdin.readline

n,m=map(int,input().split())
time=[]
for _ in range(n):
  time.append(int(input()))
left=0
right=max(time)*m
answer=max(time)*m

while left<=right:
  mid=(left+right)//2
  people=0
  for t in time:
    people+=mid//t
  if people<m:
    left=mid+1
  else:
    right=mid-1
    answer=min(answer,mid)
print(answer)