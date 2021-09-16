n=int(input())
data=list(map(int,input().split()))
data.sort(reverse=True)
res=data[0]

for i in range(1,len(data)):
  res+=data[i]/2
if res==int(res):
  print(int(res))
else:
  print(res)