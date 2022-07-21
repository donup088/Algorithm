import sys
input = sys.stdin.readline
import heapq

def dijskstra(start):
  distance=[1e9]*(n+1)
  q=[]
  distance[start]=0
  heapq.heappush(q,(0,start))
  while q:
    d,now=heapq.heappop(q)
    if distance[now]<d:
      continue
    for i in graph[now]:
      cost=d+i[1]
      if cost<distance[i[0]]:
        distance[i[0]]=cost
        heapq.heappush(q,(cost,i[0]))
  return distance

n=int(input())
m=int(input())
graph=[[] for _ in range(n+1)]
dist=[]
for _ in range(m):
  a,b,c=map(int,input().split())
  graph[a].append((b,c))
start,end=map(int,input().split())
dist=dijskstra(start)

print(dist[end])