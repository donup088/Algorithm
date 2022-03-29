n=int(input())
h=list(map(int,input().split()))
s=[]
s=h[:]
answer=0
for i in range(1,n):
  s[i]+=s[i-1]

for i in range(1,n-1):
  answer=max(answer,2*s[-1]-h[0]-h[i]-s[i])
for i in range(1,n-1):
  answer=max(answer,s[-1]-h[-1]-h[i]+s[i-1])
for i in range(1,n-1):
  answer=max(answer,s[i]-h[0]+s[-1]-s[i-1]-h[-1])

print(answer)