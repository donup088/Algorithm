import copy

def sol(sr,sc,sd,length):
    global score
    if do[sr][sc]:
        do[sr][sc] = 0
        score += 1
    for dis in range(length-1):
        sr += dir[sd][0]
        sc += dir[sd][1]
        if not (0 <= sr < N and 0 <= sc < M):
            continue
        sol(sr, sc, sd, do[sr][sc])
      
dir={}
dir['E']=(0,1)
dir['W']=(0,-1)
dir['N']=(-1,0)
dir['S']=(1,0)

# N 행 M 열
N,M,R=map(int,input().split())
do=[list(map(int,input().split())) for _ in range(N)]
do_tmp=copy.deepcopy(do)
score=0
for _ in range(R):
  ax,ay,ad=map(str,input().split())
  ax,ay=int(ax)-1,int(ay)-1
  dx,dy=map(int,input().split())
  dx,dy=dx-1,dy-1
  if do[ax][ay]!=0:
    sol(ax,ay,ad,do[ax][ay])
    
  do[dx][dy]=do_tmp[dx][dy]

print(score)
for i in range(N):
  for j in range(M):
    if do[i][j]!=0:
      print('S',end=' ')
    else:
      print('F',end=' ')
  print()