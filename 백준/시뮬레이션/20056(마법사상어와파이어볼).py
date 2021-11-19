N,M,K=map(int,input().split())

MAP = [[[] for _ in range(N)] for _ in range(N)]
fire=[]
dx=[0,1,1,1,0,-1,-1,-1]
dy=[-1,-1,0,1,1,1,0,-1]
for _ in range(M):
  r,c,m,s,d=map(int,input().split())
  fire.append([r,c,m,s,d])

for _ in range(K):
  while fire:
    ri,ci,mi,si,di=fire.pop(0)
    xx=(ci+dx[di]*si)%N
    yy=(ri+dy[di]*si)%N
    MAP[yy][xx].append([mi,si,di])
  for y in range(N):
    for x in range(N):
      while len(MAP[y][x]) >1:
        m_sum,s_sum,odd_cnt,even_cnt,cnt=0,0,0,0,len(MAP[y][x])
        while MAP[y][x]:
          mm,ss,dd=MAP[y][x].pop(0)
          m_sum+=mm
          s_sum+=ss
          if dd % 2:
            odd_cnt+=1
          else:
            even_cnt+=1
        if odd_cnt==cnt or even_cnt==cnt:
          tmp_d=[0,2,4,6]
        else:
          tmp_d=[1,3,5,7]
        if m_sum//5:
          for d in tmp_d:
            fire.append([y,x,m_sum//5,s_sum//cnt,d])
      if len(MAP[y][x])==1:
        fire.append([y,x]+MAP[y][x].pop())
res=0
for x in fire:
  res+=x[2]
print(res)