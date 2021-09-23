def DFS(L,sum):
  global res
  if L==n:
    res=max(res,sum)
  else:
    if L+T[L]<=n:
      DFS(L+T[L],sum+P[L])
    DFS(L+1,sum)

n=int(input())
T=[]
P=[]
res=0
for _ in range(n):
  a,b=map(int,input().split())
  T.append(a)
  P.append(b)

DFS(0,0)
print(res)