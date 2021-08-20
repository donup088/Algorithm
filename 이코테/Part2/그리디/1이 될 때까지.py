a, b=map(int,input().split())
res=0
while a>=b:
  while a % b !=0:
    a-=1
    res+=1
  a=a//b
  res+=1
while a>1:
  a-=1
  res+=1
print(res)