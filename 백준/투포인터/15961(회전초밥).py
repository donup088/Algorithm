from collections import defaultdict
n,d,k,c=map(int,input().split())
foods=[]
for _ in range(n):
  foods.append(int(input()))
foods.extend(foods)
l=0
r=0
d=defaultdict(int)
answer=0

d[c]+=1

while r<k:
  d[foods[r]]+=1
  r+=1

while r<len(foods):
  answer=max(answer,len(d))
  d[foods[l]]-=1
  if d[foods[l]]==0:
    del d[foods[l]]
  d[foods[r]]+=1
  l+=1
  r+=1

print(answer)