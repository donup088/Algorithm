from collections import deque
dx=[1,0,-1,0]
dy=[0,1,0,-1]

m, n, k = map(int, input().split())
board = [[0] * n for i in range(m)]
result=[]
for i in range(k):
    x1, y1, x2, y2 = map(int, input().split())
    for j in range(y1, y2):
        for k in range(x1, x2):
            board[j][k] = 1
for i in range(m):
  for j in range(n):
    if board[i][j]==0:
      count=1
      board[i][j]=1
      q=deque()
      q.append((i,j))
      while q:
        x,y=q.popleft()
        for k in range(4):
          xx=x+dx[k]
          yy=y+dy[k]
          if 0<=xx<m and 0<=yy<n and board[xx][yy]==0:
            board[xx][yy]=1
            count+=1
            q.append((xx,yy))
      result.append(count)
result.sort()
print(len(result))
for r in result:
  print(r,end=' ')