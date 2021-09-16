n=int(input())
data=[]
res=1

for i in range(n):
  a,b=map(int,input().split())
  data.append((a,b))
data.sort(key = lambda x : (x[1],x[0]))

finish=data[0][1]
for i in range(1,n):
  if data[i][0]>=finish:
    res+=1
    finish=data[i][1]
  
print(res)