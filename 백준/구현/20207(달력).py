N=int(input())

day=[[0]*366 for _ in range(N)]

data=list()

for _ in range(N):
  s,e=map(int,input().split())
  t=e-s+1
  data.append((s,e,t))
  
data.sort(key=lambda x:(x[0],-x[2]))

for i in range(len(data)):
  s,e=data[i][0],data[i][1]
  for j in range(N):
    if 1 in day[j][s:e+1]:
      continue
    for k in range(s,e+1):
      day[j][k]=1
    break

row=0
col=0
answer=0
for i in range(366):
  flag=0
  for j in range(N):
    if day[j][i]==1:
      flag=1
      row=max(row,j+1)
  if flag:
    col+=1
  else:
    answer+=row*col
    row=0
    col=0

if flag:
  answer+=row*col

print(answer)
