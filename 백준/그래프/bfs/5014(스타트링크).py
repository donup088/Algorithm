import sys
from collections import deque

input = sys.stdin.readline

F,S,G,U,D=map(int,input().split())

visited=[0]*F

def bfs(cur):
  q=deque()
  q.append([cur,0])
  visited[cur]=1
  while q:
    x,count=q.popleft()
    if x==G-1:
      return count
    if x+U <= F-1 and visited[x+U]==0:
      q.append([x+U,count+1])
      visited[x+U]=1
    if x-D >=0 and visited[x-D]==0:
      q.append([x-D,count+1])
      visited[x-D]=1
  return 1e9

res=bfs(S-1)

if res==1e9:
  print('use the stairs')
else:
  print(res)