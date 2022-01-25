dx=[-1,0,1,0]
dy=[0,1,0,-1]
from collections import deque
def solution(maps):
    n=len(maps)
    m=len(maps[0])

    q=deque()
    q.append((0,0))
    while q:
        x,y=q.popleft()
        for i in range(4):
            xx=x+dx[i]
            yy=y+dy[i]
            if 0<=xx<n and 0<=yy<m and maps[xx][yy]==1:
                q.append((xx,yy))
                maps[xx][yy]=maps[x][y]+1
    if maps[n-1][m-1]!=1:
      return maps[-1][-1] 
    return -1