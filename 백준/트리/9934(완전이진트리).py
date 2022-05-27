import sys

input = sys.stdin.readline


k=int(input())
data=list(map(int,input().split()))
tree=[[]for _ in range(k)]

def tree_make(arr,x):
  mid=len(arr)//2
  tree[x].append(arr[mid])
  if len(arr)==1:
    return
  tree_make(arr[:mid],x+1)
  tree_make(arr[mid+1:],x+1)

tree_make(data,0)

for i in range(k):
  print(*tree[i])
  