import heapq

n=int(input())
lec=[]
res=[]
for _ in range(n):
  lec.append(list(map(int,input().split())))
lec.sort()

heapq.heappush(res, lec[0][1])

for i in range(1,n):
  #이어서 할 수 있는 경우
  if lec[i][0]>=res[0]:
    heapq.heappop(res)
    heapq.heappush(res,lec[i][1])  
  # 새로운 강의실 배정
  else:
    heapq.heappush(res,lec[i][1])
  

print(len(res))