def binary_search(start,end):
  global answer
  while start<=end:
    mid=(start+end)//2
    cur=house[0]
    count=1

    for i in range(1,len(house)):
      if house[i]>=cur+mid:
        count+=1
        cur=house[i]

    if count>=c:
      start=mid+1
      answer=mid
    else:
      end=mid-1

n,c=map(int,input().split())
house=[]
answer=0
for _ in range(n):
  house.append(int(input()))
house.sort()

start=1
end=house[-1]-house[0]

binary_search(start,end)
print(answer)