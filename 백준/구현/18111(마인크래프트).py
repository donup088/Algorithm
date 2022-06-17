import sys
input = sys.stdin.readline

#n 세로 m 가로 b 인벤토리
n,m,b=map(int,input().split())

data=[list(map(int,input().split())) for _ in range(n)]

time=1e9
height=0

for i in range(257):
  minus=0 #제거된 땅 
  plus=0 # 추가해야하는 땅
  for j in range(n):
    for k in range(m):
      if i>data[j][k]:
        minus+=(i-data[j][k])
      else:
        plus+=(data[j][k]-i)

  inventory=plus+b

  if inventory<minus:
    continue

  tmp=2*plus+minus

  if tmp<=time:
    time=tmp
    height=i

print(time,height)