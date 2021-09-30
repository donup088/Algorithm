r,c=map(int,input().split())
MAP=[]
data=[]
temp=[]

for _ in range(c):
  data.append('.')
MAP.append(data)
for _ in range(r):
  MAP.append(list(input()))
for i in range(0,r+1):
  MAP[i].insert(0,'.')
  MAP[i].append('.')
MAP.append(data)
for i in range(1,r+1):
  for j in range(1,c+1):
    cnt=0
    if MAP[i][j]=='X':
      if MAP[i-1][j]=='.':
        cnt+=1
      if MAP[i+1][j]=='.':
        cnt+=1
      if MAP[i][j-1]=='.':
        cnt+=1
      if MAP[i][j+1]=='.':
        cnt+=1
    if cnt>=3:
      temp.append((i,j))

for a,b in temp:
  MAP[a][b]='.'

minX=1e9 
maxX=0
minY=1e9
maxY=0
y=0
for i in range(r+2):
  for j in range(c+2):
    if MAP[i][j]=='X':
      minX=min(minX,i)
      minY=min(minY,j)
      maxX=max(maxX,i)
      maxY=max(maxY,j)
for i in range(minX,maxX+1):
  for j in range(minY,maxY+1):
    print(MAP[i][j],end='')
  print()