n=int(input())
dx=[-1,0,1,0]
dy=[0,-1,0,1]
likes=[]
likes_slice=[[] for _ in range(n*n+1)]
stu=[[0] * n for _ in range(n)]
res = [[0 for i in range(n)] for j in range(n)]
total=0
for i in range(n*n):
  data=list(map(int,input().split()))
  likes.append(data)
  likes_slice[data[0]].append(data[1:])

for i in range(n*n):
  temp=[]
  for x in range(n):
    for y in range(n):
      if stu[x][y]==0:
        like=0
        empty=0
        for k in range(4):
          xx=x+dx[k]
          yy=y+dy[k]
          if xx < 0 or xx >= n or yy < 0 or yy >= n:
            continue
          if  stu[xx][yy] in likes[i][1:]:
            like += 1
          if stu[xx][yy] == 0:
            empty += 1
        temp.append((like,empty,(x,y)))
  temp.sort(key = lambda x : (-x[0], -x[1], x[2]))
  stu[temp[0][2][0]][temp[0][2][1]] = likes[i][0]

for i in range(n):
  for j in range(n):
    cur=stu[i][j]
    cnt=0
    for k in range(4):
      xx=i+dx[k]
      yy=j+dy[k]
      if xx < 0 or xx >= n or yy < 0 or yy >= n:
        continue
      if stu[xx][yy] in likes_slice[cur][0]:
        cnt += 1
    res[i][j] = cnt

for i in range(n):
  for j in range(n):
    if res[i][j] == 1:
      total += 1
    elif res[i][j] == 2:
      total += 10
    elif res[i][j] == 3:
      total += 100
    elif res[i][j] == 4:
      total += 1000
print(total)