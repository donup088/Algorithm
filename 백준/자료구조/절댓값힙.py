import sys
import heapq

input = sys.stdin.readline

n=int(input())
hq=[]
for _ in range(n):
  x=int(input())
  if x<0:
    heapq.heappush(hq,(-x,x))
  elif x>0:
    heapq.heappush(hq,(x,x))
  elif x==0:
    if hq:
      print(heapq.heappop(hq)[1])
    else:
      print(0)