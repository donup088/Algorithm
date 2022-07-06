n=int(input())
A=list(map(int,input().rstrip()))
B=list(map(int,input().rstrip()))

zero_changed=A[:]

zero_changed[0]=1-zero_changed[0]
zero_changed[1]=1-zero_changed[1]

def flip(arr):
  count=0
  for i in range(1,n):
    if arr[i-1]!=B[i-1]:
      arr[i-1]=1-arr[i-1]
      arr[i]=1-arr[i]
      if i!=n-1:
        arr[i+1]=1-arr[i+1]
      count+=1
  if arr==B:
    return count
  return 1e9

result1=flip(A[:])
result2=flip(zero_changed)
answer=min(result1,result2+1)

if answer==1e9:
  print(-1)
else:
  print(answer)