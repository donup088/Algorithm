n=int(input())

arr=[]
for i in range(n):
  data=input().split()
  arr.append((data[0],int(data[1])))

arr=sorted(arr,key=lambda s: s[1])

for s in arr:
  print(s[0],end=' ')