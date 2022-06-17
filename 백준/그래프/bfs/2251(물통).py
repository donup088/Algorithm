import sys
from collections import deque

input = sys.stdin.readline

def fill(x,y):
  if not visited[x][y]:
    visited[x][y]=1
    q.append([x,y])

def bfs():
  while q:
    x,y=q.popleft()
    z=c-x-y
    if x==0:
      answer.append(z)
    #x -> y
    water=min(x,b-y)
    fill(x-water,y+water)

    #x -> z
    water=min(x,c-z)
    fill(x-water,y)
  
    #y -> x  
    water=min(y,a-x)
    fill(x+water,y-water)

    #y -> z
    water=min(y,c-z)
    fill(x,y-water)

    # z -> x
    water=min(z,a-x)
    fill(x+water,y)

    # z -> y
    water=min(z,b-y)
    fill(x,y+water)

a, b, c = map(int,input().split())

q = deque()
q.append([0, 0])

visited = [[0] * 201 for _ in range(201)]
visited[0][0] = 1

answer = []

bfs()

answer.sort()
print(*answer)