from collections import deque
dx=[-1,0,1,0]
dy=[0,1,0,-1]
N=int(input())
space=[]
cx,cy=0,0
size=2
eat_time=0
for _ in range(N):
  space.append(list(map(int,input().split())))

for i in range(N):
  for j in range(N):
    if space[i][j]==9:
      cx,cy=i,j
space[cx][cy]=0
fish_count=0
while True:
  can_eat=0
  q=deque()
  q.append((cx,cy))
  visited=[[0]*N for _ in range(N)]
  dis=[[0]*N for _ in range(N)]
  visited[cx][cy]=1
  eat_list=[]
  while q:
    x,y=q.popleft()
    for i in range(4):
      xx=x+dx[i]
      yy=y+dy[i]
      if 0<=xx<N and 0<=yy<N and visited[xx][yy]==0:   
        if space[xx][yy]!=0:
          if space[xx][yy]<=size:
            visited[xx][yy]=1
            dis[xx][yy]=dis[x][y]+1
            q.append((xx,yy))
            if space[xx][yy]<size:
              eat_list.append((xx,yy,dis[xx][yy]))
              can_eat=1
        else:
          visited[xx][yy]=1
          dis[xx][yy]=dis[x][y]+1
          q.append((xx,yy))
  
  if can_eat==0:
    break
  
  eat_list=sorted(eat_list,key=lambda x:(x[2],x[0],x[1]))
  ex,ey,et=eat_list[0] 
  space[ex][ey]=0
  eat_time+=et
  fish_count+=1
  if fish_count==size:
    size+=1
    fish_count=0
  cx,cy=ex,ey
  
print(eat_time)