n=int(input())
limit=map(int,input().split())
res=0
cnt=0

for i in limit:
  cnt+=1
  if cnt>=i:
    res+=1
    cnt=0
print(res)