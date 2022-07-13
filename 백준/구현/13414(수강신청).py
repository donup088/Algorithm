import sys
input = sys.stdin.readline

k,l=map(int,input().split())

d={}
tmp=0
for _ in range(l):
  student=input().strip()
  if d.get(student)==None:
    d[student]=tmp    
  else:
    d[student]=tmp
  tmp+=1
d1 = sorted(d.items(), key=lambda x: x[1])

answer=d1[:k]
for a in answer:
  print(a[0])