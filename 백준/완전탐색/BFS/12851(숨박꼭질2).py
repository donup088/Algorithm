import sys
from collections import deque
input = sys.stdin.readline

n,k=map(int,input().split())
visited=[[-1,0] for _ in range(100001)]
q=deque()
q.append(n)
visited[n][0]=0 #시간
visited[n][1]=1 #경우의수

while q:
  now=q.popleft()
  for i in (now-1,now+1,now*2):
    if 0<=i<100001:
      if visited[i][0]==-1:
        visited[i][0]=visited[now][0]+1
        visited[i][1]=visited[now][1]
        q.append(i)
      elif visited[i][0]==visited[now][0]+1:
        visited[i][1]+=visited[now][1]
  
print(visited[k][0])
print(visited[k][1])