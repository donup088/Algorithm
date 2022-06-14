import sys
sys.stdin = open("input.txt", "r")

input = sys.stdin.readline

from itertools import combinations

l,c=map(int,input().split())
words=list(input().split())
mo=[]
ja=[]
tmp=[]
result=[]
for word in words:
  if word in ['a','e','i','o','u']:
    mo.append(word)
  else:
    ja.append(word)
if len(mo)>0:
  mo_combs=[]
  for i in range(1,len(mo)+1):
    com=combinations(mo,i)
    for c in com:
      mo_combs.append(c)
  
  for m in mo_combs:
    diff=l-len(m) ## 자음으로 채워야하는 개수
    if diff>=2 and len(ja)>=2:
      ja_combs=combinations(ja,diff)
      for j in ja_combs:
        tmp.append(list(m+j))
  
  for r in tmp:
    r.sort()
    result.append("".join(r))
    result.sort()
  
  for r in result:
    print(r)