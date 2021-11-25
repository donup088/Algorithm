import heapq

N=int(input())

arr=[]
for _ in range(N):
  s,e=map(int,input().split())
  arr.append((s,e))
arr.sort()

end=[arr[0][1]]
print(end)
arr=arr[1:]

for i in range(len(arr)):
  if arr[i][0]<end[0]:
    heapq.heappush(end,arr[i][1])
  else:
    heapq.heapreplace(end,arr[i][1])

print(len(end))