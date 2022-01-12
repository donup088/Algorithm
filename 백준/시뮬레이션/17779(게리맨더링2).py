def sol(x,y,d1,d2):
  temp=[[0]*(N+1) for _ in range(N+1)]
  temp[x][y]=5
  for i in range(1,d1+1):
    temp[x+i][y-i]=5
  for i in range(1,d2+1):
    temp[x+i][y+i]=5
  for i in range(1,d2+1):
    temp[x+d1+i][y-d1+i]=5
  for i in range(1,d1+1):
    temp[x+d2+i][y+d2-i]=5

  count=[0]*5

  for r in range(1,x+d1):
    for c in range(1,y+1):
      if temp[r][c]==5:
        break
      else:
        count[0]+=MAP[r][c]
  
  for r in range(1,x+d2+1):
    for c in range(N,y,-1):
      if temp[r][c]==5:
        break
      else:
        count[1]+=MAP[r][c]
  
  for r in range(x+d1,N+1):
    for c in range(1,y-d1+d2):
      if temp[r][c]==5:
        break
      else:
        count[2]+=MAP[r][c]
  
  for r in range(x+d2+1,N+1):
    for c in range(N,y-d1+d2-1,-1):
      if temp[r][c]==5:
        break
      else:
        count[3]+=MAP[r][c]
  
  count[4]=total-sum(count)
  return max(count)-min(count)

N=int(input())
MAP=[]
total=0
ans=1e9

MAP.append([0]*(N+1))

for _ in range(N):
  a=[0]+list(map(int,input().split()))
  MAP.append(a)
  total+=sum(a)

for x in range(1,N+1):
  for y in range(1,N+1):
    for d1 in range(1,N-1):
      for d2 in range(1,N-1):
        if x+d1+d2>N :
          continue
        if y-d1<1:
          continue
        if y+d2>N:
          continue
        ans=min(ans,sol(x,y,d1,d2))

print(ans)