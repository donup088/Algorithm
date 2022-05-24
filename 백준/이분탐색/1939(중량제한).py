import sys
from collections import deque

input = sys.stdin.readline

def bfs(mid):
  q=deque()
  q.append(start)
  visited=[0]*(n+1)
  while q:
    now=q.popleft()
    for x,w in graph[now]:
      if visited[x]==0 and w>=mid:
        visited[x]=1
        q.append(x)

  if visited[end]==1:
    return True
    
  return False

n,m=map(int,input().split())
graph=[[] for _ in range(n+1)]

for _ in range(m):
  a,b,c=map(int,input().split())
  graph[a].append((b,c))
  graph[b].append((a,c))

start,end=map(int,input().split())
result=1
left=1
right=1000000000

while left<=right:
  mid=(left+right)//2
  if bfs(mid):
    result=mid
    left=mid+1
  else:
    right=mid-1

print(result)

