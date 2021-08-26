s=input()
arr=[]

for i in s:
  arr.append(int(i))

res=arr[0]
for i in range(1,len(arr)):
  if arr[i]==0 or arr[i]==1:
    res+=arr[i]
  else:
    if(res==0):
      res=1
    res=res*arr[i]
print(res)