N,M=map(int,input().split())
tree=list(map(int,input().split()))

def binary_search():
  start,end=0,max(tree)
  while start<=end:
    mid=(start+end)//2
    total=0
    for i in tree:
      if i-mid>=0:
        total+=i-mid
    if total<M:
      end=mid-1
    else:
      start=mid+1
  return end

print(binary_search())