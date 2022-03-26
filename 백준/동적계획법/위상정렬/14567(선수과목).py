from collections import deque

n,m=map(int,input().split())

indegree=[0]*(n+1)
graph=[[] for _ in range(n+1)]
answer=[1 for _ in range(n+1)]

for _ in range(m):
  a,b=map(int,input().split())
  graph[a].append(b)
  # 진입 차수 1 증가
  indegree[b]+=1

#위상정렬
def topology_sort():
  q=deque()
  for i in range(1,n+1):
    if indegree[i]==0:
      q.append(i)
      answer[i]=1
      
  while q:
    now=q.popleft()
    for i in graph[now]:
      indegree[i]-=1
      if indegree[i]==0:
        q.append(i)
      answer[i]=answer[now]+1

  print(*answer[1:])

topology_sort()