import sys
from collections import deque

input = sys.stdin.readline

n,q=map(int,input().split())
graph = [[] for _ in range(n+1)]

for _ in range(n-1):
    a, b, u = (map(int, input().split()))
    graph[a].append((b, u))
    graph[b].append((a, u))
  
for i in range(q):
    k, v = map(int, input().split())
    visited=[0]*(n+1)
    visited[v]=1
    q=deque()
    q.append([v,1e9])
    count=0
    while q:
      node,u=q.popleft()
      for next_node,next_u in graph[node]:
        next_u=min(u,next_u)
        if next_u>=k and visited[next_node]==0:
          q.append((next_node,next_u))
          count+=1
          visited[next_node]=1
    print(count)