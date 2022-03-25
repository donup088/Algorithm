n,m=map(int,input().split())
d=set()
b=set()
for _ in range(n):
  d.add(input())

for _ in range(m):
  b.add(input())

res=list(d&b)
res.sort()
print(len(res))
for r in res:
  print(r)