import sys
input = sys.stdin.readline

N=int(input())
M=int(input())

if M:
  broken=set(input().split())
else:
  broken=set()

answer=abs(100-N)

for num in range(1000001):
  for n in str(num):
    if n in broken:
      break
  else:
    answer=min(answer,len(str(num))+abs(num-N))
print(answer)