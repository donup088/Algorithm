import sys
input = sys.stdin.readline
import heapq

dx=[-1,0,1,0]
dy=[0,1,0,-1]
def bfs():
  while q:
    time,value,x,y=heapq.heappop(q)
    if time==s:
      break
    for i in range(4):
      xx,yy=x+dx[i],y+dy[i]
      if 0<=xx<n and 0<=yy<n and arr[xx][yy]==0:
        heapq.heappush(q,[time+1,value,xx,yy])
        arr[xx][yy]=arr[x][y]

        
n,k=map(int,input().split())
arr=[list(map(int,input().split())) for _ in range(n)]
s,x,y=map(int,input().split())
q=[]
for i in range(n):
  for j in range(n):
    if arr[i][j]!=0:
      heapq.heappush(q,[0,arr[i][j],i,j])

bfs()

print(arr[x-1][y-1])