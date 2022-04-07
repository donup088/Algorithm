import sys
sys.stdin = open("input.txt", "r")

sys.setrecursionlimit(10**6)
input=sys.stdin.readline

def dfs(x,y):
  global answer
  if x==m-1 and y==n-1:
    return 1
  if visited[x][y]!=-1:
    return visited[x][y]
  visited[x][y]=0
  for i in range(4):
    xx=x+dx[i]
    yy=y+dy[i]
    if 0<=xx<m and 0<=yy<n:
      if board[xx][yy]<board[x][y]:
        visited[x][y]+=dfs(xx,yy)
  return visited[x][y]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
# m 세로 n 가로
m,n=map(int,input().split())
board=[list(map(int,input().split())) for _ in range(m)]

visited = list([-1] * n for _ in range(m))

print(dfs(0,0))