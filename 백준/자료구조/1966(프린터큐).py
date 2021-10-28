from collections import deque

cnt=int(input())
for i in range(cnt):
  N,M=map(int,input().split())
  q=deque()
  b=list(map(int,input().split()))
  for j in range(len(b)):
    q.append((b[j],j))
    res=1
  while True:
    maxQ=0
    for i in range(len(q)):
      if maxQ<q[i][0]:
        maxQ=q[i][0]

    if q[0][0]==maxQ:
      if q[0][1]==M:
        print(res)
        break
      else:
        q.popleft()
        res+=1
    else:
      q.rotate(-1)
      