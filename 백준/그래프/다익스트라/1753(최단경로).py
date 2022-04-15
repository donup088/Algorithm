import heapq

def dijskstra(start):
  distance=[1e9]*(v+1)
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

v,e=map(int,input().split())
k=int(input())
graph=[[] for _ in range(v+1)]
dist=[]
for _ in range(e):
  a,b,c=map(int,input().split())
  graph[a].append((b,c))

dist=dijskstra(k)

for i in range(1,len(dist)):
  if dist[i]==1e9:
    print('INF')
  else:
    print(dist[i])