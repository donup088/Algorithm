import sys
sys.stdin = open("input.txt", "r")

n=int(input())
data=[]
for _ in range(n):
  data.append(input().split())
  
data.sort(key=lambda x: (-int(x[1]),int(x[2]),-int(x[3]),x[0]))

for x in data:
  print(x[0])
