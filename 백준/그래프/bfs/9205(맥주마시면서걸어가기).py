import sys
input = sys.stdin.readline
from collections import deque

def bfs(cx,cy):
  q=deque()
  q.append([cx,cy])
  while q:
    x,y=q.popleft()
    if abs(dx-x)+abs(dy-y)<=1000:
      print('happy')
      return
    for i in range(n):
      if visited[i]==0:
        xx,yy=store[i]
        if abs(x-xx)+abs(y-yy)<=1000:
          q.append([xx,yy])
          visited[i]=1
  print('sad')
  
t=int(input())
for _ in range(t):
  n=int(input())
  cx,cy=map(int,input().split())
  store=[]
  for _ in range(n):
    x,y=map(int,input().split())
    store.append([x,y])
  
  dx,dy=map(int,input().split())

  visited=[0]*(n+1)

  bfs(cx,cy)