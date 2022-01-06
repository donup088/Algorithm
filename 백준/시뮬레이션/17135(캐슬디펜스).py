import sys
sys.stdin = open("input.txt", "r")
from itertools import combinations
from copy import deepcopy

N,M,D=map(int,input().split())
castle = []
enemy=set()
for y in range(N):
  arr=list(map(int,input().split()))
  for x in range(M):
    if arr[x]==1:
      enemy.add((y,x))

for i in range(M):
  castle.append((N,i))

MAP=[[0 for _ in range(M)] for _ in range(N)]

archors=combinations(castle,3)

def possible_shot(maps,combs):
  area=[]
  for com in combs:
    copied=[]
    for y in range(N):
      for x in range(M):
        dis=abs(com[0]-y)+abs(com[1]-x)
        if dis<=D:
          copied.append((dis,y,x))  
    area.append(copied)

  return area

def find_enemy(area,enemy):
  area.sort(key=lambda x:(x[0],x[2]))
  for dis,y,x in area:
    if (y,x) in enemy:
      return (y,x)
  return None

def move(enemy):
  return set([(y+1,x) for y,x in enemy if y+1<N])

ans=0

for archor in archors:
  possible_area=possible_shot(MAP,archor)
  count=0
  copy_enemy=deepcopy(enemy)
  while enemy:
    tmp=set()
    for area in possible_area:
      kill=find_enemy(area,enemy)
      if kill is not None:
        tmp.add(kill)
    count+=len(tmp)
    enemy-=tmp
    enemy=move(enemy)

  enemy=copy_enemy
  
  if ans<count:  
    ans=count
print(ans)