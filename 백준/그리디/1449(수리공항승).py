import sys
input = sys.stdin.readline

n,l=map(int,input().split())
data=list(map(int,input().split()))

data.sort()

start=data[0]
count=1

for i in range(1,len(data)):
  if start<=data[i]<start+l:
    continue
  else:
    start=data[i]
    count+=1
print(count)