from collections import deque

N,M=map(int,input().split())
train=[deque([0]*20) for _ in range(N)]
res=[]

for _ in range(M):
  data=list(map(int,input().split()))
  if data[0]==1:
    train[data[1]-1][data[2]-1]=1
  elif data[0]==2:
    train[data[1]-1][data[2]-1]=0
  elif data[0]==3:
    train[data[1]-1].rotate(1)
    train[data[1]-1][0]=0
  else:
    train[data[1]-1].rotate(-1)
    train[data[1]-1][19]=0

for q in train:
  if q not in res:
    res.append(q)
print(len(res))