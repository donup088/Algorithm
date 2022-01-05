n=int(input())
dx=[1,0,-1,0]
dy=[0,-1,0,1]

dots=[]
ans=0

def rotate(x,y,i,j):
  xx=i-(y-j)
  yy=j+(x-i)
  return xx,yy

def move(arr):
  tmp=[]
  for i in range(len(arr)-1): #모든 점들을 회전시킨다.
    xx,yy=rotate(arr[i][0],arr[i][1],arr[-1][0],arr[-1][1])
    tmp.append([xx,yy])
  tmp.reverse() # 제일 처음 더해진 점이 마지막점이기 때문에 기준점을 잡기 위해 reverse 사용
  return arr+tmp

for _ in range(n):
  x,y,d,g=map(int,input().split())
  xx=x+dx[d]
  yy=y+dy[d]
  tmp=[[x,y],[xx,yy]]
  for i in range(g):
    tmp=move(tmp)
  for k in tmp:
    if [k[0],k[1]] not in dots:
      dots.append(k)

ddx=[-1,-1,0]
ddy=[0,1,1]
for i in range(len(dots)):
  x,y=dots[i]
  flag=True
  for j in range(3):
    if [x+ddx[j],y+ddy[j]] not in dots:
      flag=False
      break
  if flag:
    ans+=1
print(ans)