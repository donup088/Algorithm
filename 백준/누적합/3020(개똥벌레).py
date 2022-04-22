import sys

input = sys.stdin.readline

n,h=map(int,input().split())
top=[0]*(h+1)
bottom=[0]*(h+1)
cnt=n
range_cnt=0
for i in range(n):
  if i%2==0:
    bottom[int(input())]+=1
  else:
    top[int(input())]+=1

for i in range(h-1,0,-1):
  bottom[i]+=bottom[i+1]
  top[i]+=top[i+1]

for i in range(1,h+1):
  destroy=bottom[i]+top[h-i+1]
  if cnt>destroy:
    cnt=destroy
    range_cnt=1
  elif cnt==destroy:
    range_cnt+=1

print(cnt,range_cnt)