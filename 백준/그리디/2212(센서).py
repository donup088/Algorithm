N=int(input())
K=int(input())
arr=sorted(list(map(int,input().split())))
diff=[]

if K>=N:
  print(0)
else:  
  for i in range(0,N-1):
    diff.append(arr[i+1]-arr[i])
  diff.sort(reverse=True)

  for _ in range(K-1):
    diff.pop(0)

  print(sum(diff))