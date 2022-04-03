import sys

n,m=map(int,sys.stdin.readline().split())
data=[list(map(int,sys.stdin.readline().split())) for _ in range(n)]

for i in range(n):
  for j in range(n):
    if j!=0:
      data[i][j]+=data[i][j-1]

for i in range(m):
  answer=0
  x1,y1,x2,y2=map(int,sys.stdin.readline().split())
  for j in range(x1-1,x2):
    if y1!=1:
      answer-=data[j][y1-2]
    answer+=data[j][y2-1]
  print(answer)