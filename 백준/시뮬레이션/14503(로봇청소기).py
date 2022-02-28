#북동남서
dx=[-1,0,1,0]
dy=[0,1,0,-1]

#n 세로 m 가로
n,m=map(int,input().split())
r,c,d=map(int,input().split())
board=[list(map(int,input().split())) for _ in range(n)]
visited=[[0]*m for _ in range(n)]
visited[r][c]=1
res=1

while True:
  flag=0
  for _ in range(4):
    xx=r+dx[(d+3)%4]
    yy=c+dy[(d+3)%4]
    d=(d+3)%4
    if 0<=xx<n and 0<=yy<m and board[xx][yy]==0:
      if visited[xx][yy]==0:
        visited[xx][yy]=1
        res+=1
        r=xx
        c=yy
        flag=1
        break
  if flag==0:
    if board[r-dx[d]][c-dy[d]]==1:
      print(res)
      break
    else:
      r,c=r-dx[d],c-dy[d]