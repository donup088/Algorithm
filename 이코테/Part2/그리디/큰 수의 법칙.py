a, b, c =map(int ,input().split());
data=list(map(int,input().split()));

data.sort();
m1=data[a-1]
m2=data[a-2]
res=[]
sum=0
while(True):
  if(len(res)==b):
    break;
  for _ in range(c):
    sum+=m1
    res.append(m1)
  sum+=m2
  res.append(m2)
print(sum)

  

   