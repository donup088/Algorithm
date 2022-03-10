from itertools import permutations

n=int(input())
number=list(map(int,input().split()))
pl,mi,mul,div=map(int,input().split())
oper=['+']*pl+['-']*mi+['*']*mul+['/']*div
per=list(permutations(oper,n-1))
result=[]
for j in range(len(per)):
  res=number[0]
  for i in range(1,n):
    op=per[j][i-1]
    if op=='+':
      res+=number[i]
    elif op=='-':
      res-=number[i]
    elif op=='*':
      res*=number[i]
    elif op=='/':
      if res<0:
        res=-(abs(res)//number[i])
      else:
        res=res//number[i]
  result.append(res)
print(max(result))
print(min(result))