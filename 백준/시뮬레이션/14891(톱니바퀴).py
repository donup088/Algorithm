from collections import deque
data=[]
res=0
for i in range(4):
  data.append(deque(input()))

K=int(input())
for _ in range(K):
  q=deque()
  visited=[0]*4
  a,b=map(int,input().split())
  q.append((a-1,b,data[a-1][6],data[a-1][2]))
  visited[a-1]=1
  data[a-1].rotate(b)
  while q:
    n,d,l,r=q.popleft()
    if n-1>=0 and data[n-1][2]!=l and visited[n-1]==0:
      visited[n-1]=1
      q.append((n-1,-d,data[n-1][6],data[n-1][2]))
      data[n-1].rotate(-d)
    if n+1<4 and data[n+1][6]!= r and visited[n+1]==0:
      visited[n+1]=1
      q.append((n+1,-d,data[n+1][6],data[n+1][2]))
      data[n+1].rotate(-d)

for i in range(4):
  if data[i][0]=='1':
    res+=2**i
print(res)