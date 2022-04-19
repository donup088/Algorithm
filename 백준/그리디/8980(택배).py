n,c=map(int,input().split())
m=int(input())
data=[list(map(int,input().split())) for _ in range(m)]
data.sort(key=lambda x:x[1])
box=[c]*(n+1)
answer=0

for s,e,b in data:
  _min=c
  for i in range(s,e):
    _min=min(_min,box[i])
  _min=min(_min,b)
  for i in range(s,e):
    box[i]-=_min
  answer+=_min

print(answer)