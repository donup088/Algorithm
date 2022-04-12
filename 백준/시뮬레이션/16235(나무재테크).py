from collections import deque

dx=[1,0,-1,0,1,1,-1,-1]
dy=[0,1,0,-1,1,-1,1,-1]

def spring_summer():
  for i in range(n):
    for j in range(n):
      t_l=len(tree[i][j])
      for k in range(t_l):
        if tree[i][j][k]<=nutrients[i][j]:
          nutrients[i][j]-=tree[i][j][k]
          tree[i][j][k]+=1
        else:
          for _ in range(k,t_l):
            nutrients[i][j]+=tree[i][j].pop()//2
          break

def fall_winter():
  for i in range(n):
    for j in range(n):
      for k in tree[i][j]:
        if k%5==0:
          for l in range(8):
            xx=i+dx[l]
            yy=j+dy[l]
            if 0<=xx<n and 0<=yy<n:
              tree[xx][yy].appendleft(1)
      nutrients[i][j]+=a[i][j]
          
n,m,k=map(int,input().split())
nutrients=[[5]*n for _ in range(n)]
a=[list(map(int,input().split())) for _ in range(n)]
tree=[[deque() for _ in range(n)] for _ in range(n)]
answer=0

for _ in range(m):
  x,y,age=map(int,input().split())
  tree[x-1][y-1].append(age)
  
for i in range(k):
  spring_summer()
  fall_winter()
  
for i in range(n):
  for j in range(n):
    answer+=len(tree[i][j])
print(answer)