import sys
from collections import deque

sys.stdin=open("input.txt","r")

n,m=map(int,input().split())
graph=[]
for i in range(n):
  graph.append(list(map(int,input())))

dx=[-1,1,0,0]
dy=[0,0,-1,1]

q=deque()
q.append((0,0))
while q:
  x,y=q.popleft()
  for i in range(4):
    xx=x+dx[i]
    yy=y+dy[i]
    if xx>=0 and yy>=0 and xx<n and yy<m and graph[xx][yy]==1:
      graph[xx][yy]=graph[x][y]+1
      q.append((xx,yy))
print(graph[n-1][m-1])
