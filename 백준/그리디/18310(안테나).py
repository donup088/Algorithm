n=int(input())
arr=list(map(int,input().split()))
arr.sort()
if len(arr)%2==1:
  print(arr[len(arr)//2])
else:
  idx=len(arr)//2
  left=arr[idx-1]
  left_sum=0
  right=arr[idx]
  right_sum=0
  answer=[]
  for a in arr:
    left_sum+=abs(a-left)
    right_sum+=abs(a-right)
  if left_sum<=right_sum:
    answer.append(left)
  else:
    answer.append(right)
  print(min(answer))