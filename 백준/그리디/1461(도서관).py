import sys
input = sys.stdin.readline

n,m=map(int,input().split())
books=list(map(int,input().split()))
minus=[]
plus=[]

answer=0
for b in books:
  if b<0:
    minus.append(b)
  else:
    plus.append(b)

minus.sort()
plus.sort(reverse=True)
m_max=0
p_max=0
while minus:
  tmp=[]
  for _ in range(m):
    if minus:
      mp=minus.pop(0)
      tmp.append(abs(mp))
  m_max=max(max(tmp),m_max)
  answer+=max(tmp)*2
  
while plus:
  tmp=[]
  for _ in range(m):
    if plus:
      pp=plus.pop(0)
      tmp.append(abs(pp))
  p_max=max(max(tmp),p_max)
  answer+=max(tmp)*2
  
print(answer-max(p_max,m_max))