import sys
from collections import deque
input = sys.stdin.readline

n,k=map(int,input().split())
visited=[-1]*100001
q=deque()
q.append(n)
visited[n]=0

while q:
  now=q.popleft()
  if now==k:
    print(visited[now])
    break
  for i in (now-1,now+1,now*2):
    if 0<=i<100001 and visited[i]==-1:
      visited[i]=visited[now]+1
      q.append(i)