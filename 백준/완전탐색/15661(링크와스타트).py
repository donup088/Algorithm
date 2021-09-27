from itertools import combinations

n=int(input())
arr=[]
res=1e9
num=[i for i in range(n)]
for i in range(n):
  arr.append(list(map(int,input().split())))
combs=list(combinations(num,n//2))

for comb in combs:
  start=0
  link=0
  remains=[i for i in range(n) if i not in comb]
  for com in combinations(comb,2):
    start+=arr[com[0]][com[1]]+arr[com[1]][com[0]]
  for remain in combinations(remains,2):
    link+=arr[remain[0]][remain[1]]+arr[remain[1]][remain[0]]
  res=min(res,abs(start-link))
print(res)