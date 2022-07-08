import sys

sys.stdin = open("input.txt", "r")

input = sys.stdin.readline

n,m,r=map(int,input().split())

graph=[[] for _ in range(n+1)]
visited=[0]*(n+1)
answer=[0]*(n+1)
count=1
for i in range(m):
  u,v=map(int,input().split())
  graph[u].append(v)
  graph[v].append(u)

def dfs(cur):
  global count
  visited[cur]=1
  graph[cur].sort(reverse=True)
  answer[cur]=count
  for x in graph[cur]:
    if visited[x]==0:
      count+=1
      dfs(x)

dfs(r)

for a in answer[1:]:
  print(a)