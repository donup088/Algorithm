def vertical_flip():
  tmp = [[0] * M for _ in range(N)]
  for i in range(N):
    for j in range(M):
      tmp[i][j] = data[N-1-i][j]
  return tmp

def horizontal_flip():
  tmp = [[0] * M for _ in range(N)]
  for i in range(N):
    for j in range(M):
      tmp[i][j] = data[i][M-1-j]
  return tmp

def rotate_right(arr):
  #N=세로
  #M=가로
  tmp = [[0] * N for _ in range(M)]
  for i in range(N):
    for j in range(M):
      tmp[j][N-1-i] = arr[i][j]
  return tmp

def rotate_left(arr):
  tmp = [[0] * N for _ in range(M)]
  for i in range(M):
    for j in range(N):
      tmp[i][j] = arr[j][M-i-1]
  return tmp

def group1():
  tmp = [[0] * M for _ in range(N)]
  for i in range(N//2):
    for j in range(M//2):
      tmp[i][j+M//2]=data[i][j]
  for i in range(N//2):
    for j in range(M//2,M):
      tmp[i+N//2][j]=data[i][j]
  for i in range(N//2,N):
    for j in range(M//2,M):
      tmp[i][j-M//2]=data[i][j]
  for i in range(N//2,N):
    for j in range(M//2):
      tmp[i-N//2][j]=data[i][j]
  return tmp

def group2():
  tmp = [[0] * M for _ in range(N)]
  for i in range(N//2):
    for j in range(M//2):
      tmp[i+N//2][j]=data[i][j]
  for i in range(N//2,N):
    for j in range(M//2):
      tmp[i][j+M//2]=data[i][j]
  for i in range(N//2,N):
    for j in range(M//2,M):
      tmp[i-N//2][j]=data[i][j]
  for i in range(N//2):
    for j in range(M//2,M):
      tmp[i][j-M//2]=data[i][j]
  return tmp

N,M,R=map(int,input().split())
data=[]
for _ in range(N):
  data.append(list(map(int,input().split())))
action=list(map(int,input().split()))

for a in action:
  if a==1:
    data=vertical_flip()
  elif a==2:
    data=horizontal_flip()
  elif a==3:
    data=rotate_right(data)
    N,M=M,N
  elif a==4:
    data=rotate_left(data)
    N,M=M,N
  elif a==5:
    data=group1()
  else:
    data=group2()
for i in range(len(data)):
  for j in range(len(data[i])):
    print(data[i][j],end=' ')
  print()