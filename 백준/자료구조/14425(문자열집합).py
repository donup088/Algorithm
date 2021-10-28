N,M=map(int,input().split())

res=0
dic={}
for i in range(N):
  s=input()
  dic[s]=1
for i in range(M):
  s=input()
  if s in dic:
    res+=1
print(res)