n=input().split('-')
res=0
plus=n[0].split('+')
minus=n[1:]
for x in plus:
  res+=int(x)
for a in minus:
  for b in a.split('+'):
    res-=int(b)
print(res)
