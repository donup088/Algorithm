import sys
sys.stdin=open("input.txt","r")

dx=[-1,0,1,0]
dy=[0,1,0,-1]

n,m=map(int,input().split())
data=[]
temp=[[0]*m for _ in range(n)]
result=0
for _ in range(n):
  data.append(list(map(int,input().split())))

def getSum():
  sum=0
  for i in range(n):
    for j in range(m):
      if temp[i][j]==0:
        sum+=1
  return sum

def virus(x,y):
  for i in range(4):
    xx=x+dx[i]
    yy=y+dy[i]
    if 0<=xx<n and 0<=yy<m:
      if temp[xx][yy]==0:
        temp[xx][yy]=2
        virus(xx,yy)

def dfs(count):
  global result
  if count==3:
    for i in range(n):
      for j in range(m):
        temp[i][j]=data[i][j]
    for i in range(n):
      for j in range(m):
        if temp[i][j]==2:
          virus(i,j)
    result=max(result,getSum())
    return 
  for i in range(n):
    for j in range(m):
      if data[i][j]==0:
        data[i][j]=1
        count+=1
        dfs(count)
        data[i][j]=0
        count-=1
dfs(0)
print(result)