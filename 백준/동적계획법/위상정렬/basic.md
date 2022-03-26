## 위상정렬
- 사이클이 없는 방향 그래프의 모든 노드를 방향성에 거스르지 않도록 순서대로 나열하는 것
- ex) 선수과목을 고려한 학습 순서 설정

- 구현과정
1. 진입차수가 0인 모든 노드를 큐에 넣는다.
2. 큐가 빌 때까지 다음의 과정을 반복한다.
    1. 큐에서 원소를 꺼내 해당 노드에서 나가는 간선을 그래프에서 제거한다.
    2. 새롭게 진입차수가 0이 된 노드를 큐에 넣는다.

```
v,e=map(int,input().split())
indegree=[0] * (v+1)
graph=[[] for _ in range(v+1)]

for _ in range(e):
  a,b=map(int,input().split())
  graph[a].append(b) # a에서 b로 이동가능
  # 진입 차수 증가
  indegree[b]+=1

def topology_sort():
  result=[]
  q=deque()
  # 진입 차수가 0인 노드 큐에 삽입
  for i in range(1,v+1):
    if indegree[i]==0:
      q.append(i)

  while q:
    now=q.popleft()
    result.append(now)
    for i in graph[now]:
      indegree[i]-=1
      if indegree[i]==0:
        q.append(i)

  for i in result:
    print(i, end=' ')

topology_sort()
```