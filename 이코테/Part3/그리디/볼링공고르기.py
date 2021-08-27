import sys
sys.stdin=open("input.txt","r")

n,m=map(int,input().split())
k=list(map(int,input().split()))

res=0

for i in range(n):
  for j in range(i+1,len(k)):
    if k[i]!=k[j]:
      res+=1

print(res)