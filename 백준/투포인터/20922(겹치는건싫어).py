n,k=map(int,input().split())
numbers=list(map(int,input().split()))

l,r=0,0
count=[0]*(max(numbers)+1)
answer=0
while r<n:
  if count[numbers[r]]<k:
    count[numbers[r]]+=1
    r+=1
  else:
    count[numbers[l]]-=1
    l+=1
  answer=max(answer,r-l)
print(answer)