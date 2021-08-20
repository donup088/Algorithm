a=input()
x=int(a[1])
y=int(ord(a[0]))-96
directions=[(2,1),(-2,1),(2,-1),(-2,-1),(1,2),(-1,2),(1,-2),(-1,-2)]

res=0
for d in directions:
  xx=x+d[0]
  yy=y+d[1]
  if xx>=1 and xx<=8 and yy>=1 and yy<=8:
    res+=1
print(res)