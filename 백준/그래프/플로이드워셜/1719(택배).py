n,m=map(int,input().split())
graph=[[1e9]*(n+1) for _ in range(n+1)]
answer=[[0]*(n+1) for _ in range(n+1)]

for i in range(n+1):
  for j in range(n+1):
    if i==j:
      graph[i][j]=0
      answer[i][j]=1e9
      
for _ in range(m):
  a,b,c=map(int,input().split())
  graph[a][b]=c
  graph[b][a]=c
  answer[a][b]=b
  answer[b][a]=a
  
for k in range(1,n+1):
  for i in range(1,n+1):
    for j in range(1,n+1):
      if graph[i][j]>graph[i][k]+graph[k][j]:
        graph[i][j]=graph[i][k]+graph[k][j]
        answer[i][j]=answer[i][k]

for i in range(1,n+1):
  for j in range(1,n+1):
    if answer[i][j]==1e9:
      print('-',end=' ')
    else:
      print(answer[i][j],end=' ')
  print()