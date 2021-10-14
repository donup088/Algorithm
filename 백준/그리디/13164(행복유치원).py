n,k=map(int,input().split())
student=list(map(int,input().split()))
diff=[]
res=0
for i in range(n-1):
  dif=student[i+1]-student[i]
  diff.append(dif)

diff.sort()

for i in range(n-k):
  res+=diff[i]
print(res)