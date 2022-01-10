N=int(input())
M=int(input())
action=[]
for _ in range(M):
  action.append(list(map(int,input().split())))

wall=[0]+[1]*(N-1)
for i in range(M):
  x,y=action[i]
  for j in range(x,y,1):
    wall[j]=0

print(wall.count(1)+1)