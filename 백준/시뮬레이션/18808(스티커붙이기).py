# n 세로 m 가로 k 스티커 개수
n,m,k=map(int,input().split())
board=[[0]*m for _ in range(n)]
answer=0

def rotate_90(arr):
  n = len(arr)
  m = len(arr[0])

  result = [[0]* n for _ in range(m)]

  for i in range(n):
    for j in range(m):
      result[j][n-i-1] = arr[i][j]
  return result

def attach(x,y,sticker,r,c):
  for i in range(x,x+r):
    for j in range(y,y+c):
      if board[i][j] and sticker[i-x][j-y]:
        return False
  for i in range(x,x+r):
    for j in range(y,y+c):
      if sticker[i-x][j-y]:
        board[i][j]=1
  return True

def start(sticker,r,c):
  for i in range(n-r+1):
    for j in range(m-c+1):
      if attach(i,j,sticker,r,c):
        return True
  return False

for i in range(k):
  # r 행의 개수(세로) c 열의 개수(가로)
  r,c=map(int,input().split())
  sticker=[list(map(int,input().split())) for _ in range(r)]

  for _ in range(4):
    if start(sticker,r,c):
      break
    else:
      sticker=rotate_90(sticker)
      r,c=c,r

for i in range(n):
  answer+=sum(board[i])

print(answer)