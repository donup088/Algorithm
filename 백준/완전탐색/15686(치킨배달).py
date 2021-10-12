from itertools import combinations

n,m=map(int,input().split())
chicken,house=[],[]

for i in range(n):
  data=list(map(int,input().split()))
  for j in range(n):
    if data[j]==1:
      house.append((i,j))
    if data[j]==2:
      chicken.append((i,j))

comb=list(combinations(chicken,m))

def sol(com):
  res=0
  for hx,hy in house:
    temp=1e9
    for cx,cy in com:
      temp=min(temp,abs(hx-cx)+abs(hy-cy))
    res+=temp
  return res

res=1e9
for com in comb:
  res=min(res,sol(com))

print(res)