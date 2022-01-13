from itertools import combinations

N=int(input())
data=[]
team=[]
for i in range(N):
  data.append(list(map(int,input().split())))
  team.append(i)

ans=1e9
for i in range(2,N):
  combs=list(combinations(team,i))
  for com in combs:
    x,y=0,0
    remain=[]
   
    for j in team:
      if j not in com:
        remain.append(j)
    
    for k in range(len(com)):
      for z in range(k,len(com)):
        x+=data[com[k]][com[z]]+data[com[z]][com[k]]
    for k in range(len(remain)):
      for z in range(k,len(remain)):
        y+=data[remain[k]][remain[z]]+data[remain[z]][remain[k]]
   
    ans=min(ans,abs(x-y))
      
print(ans)
