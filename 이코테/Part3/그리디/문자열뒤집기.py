s=input()
res0=0
res1=0

if int(s[0])==1:
  res1+=1
else:
  res0+=1

for i in range(len(s)-1):
  if s[i]!=s[i+1]:
    if s[i+1]=='1':
      res0+=1
    else:
      res1+=1
print(min(res1,res0))