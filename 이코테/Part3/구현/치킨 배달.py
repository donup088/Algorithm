import sys
from itertools import combinations
sys.stdin=open("input.txt","r")

n,m=map(int,input().split())
house=[]
chicken=[]
data=[]
for _ in range(n):
  data.append(list(map(int,input().split())))
for i in range(n):
  for j in range(n):
    if data[i][j]==1:
      house.append((i,j))
    if data[i][j]==2:
      chicken.append((i,j))

surviveChicken=list(combinations(chicken,m))

res=2147000000

for ch in surviveChicken:
  resSum=0
  for hx,hy in house:
    tmp=2147000000
    for cx,cy in ch:
      tmp=min(tmp,abs(hx-cx)+abs(hy-cy))
    resSum+=tmp
  res=min(res,resSum)

print(res)

