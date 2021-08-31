import sys

sys.stdin=open("input.txt","r")

s=input()
digit=[]
res=[]
for i in range(len(s)):
  if s[i].isdigit()==True:
    digit.append(s[i])
  else:
    res.append(s[i])

res.sort()
res.append(sum(map(int,digit)))
for x in res:
  print(x,end="")