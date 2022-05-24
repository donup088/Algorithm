from collections import deque

dx=[-1,1]

n,k=map(int,input().split())
sam=map(int,input().split())
q=deque()
visited=set()

for i in sam:
  q.append([i,1])
  visited.add(i)

res=0
house=0
while q:
  x,bad=q.popleft()
  for i in range(2):
    xx=x+dx[i]
    if xx not in visited:
      visited.add(xx)
      house+=1
      res+=bad
      q.append([xx,bad+1])
    if house==k:
      q=list()
      break
    
print(res)