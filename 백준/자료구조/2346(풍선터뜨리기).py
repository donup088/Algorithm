from collections import deque

N=int(input())
data=list(map(int,input().split()))
q=deque()
for i in range(N):
  q.append((i,data[i]))
tmp=0
while q:
  tmp=q.popleft()
  if tmp[1]>0:
    q.rotate(-tmp[1]+1)
    print(tmp[0]+1,end=' ')
  elif tmp[1]<0:
    q.rotate(-tmp[1])
    print(tmp[0]+1,end=' ')