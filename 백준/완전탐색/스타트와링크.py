from itertools import combinations

n=int(input())
stat=[list(map(int,input().split())) for _ in range(n)]
p=[i for i in range(n)]
combs=list(combinations(p, n//2))
answer=1e9
for i in range(len(combs)):
  start_sum=0
  link_sum=0
  start=list(combs[i])
  link=list(set(p)-set(start))
  for com in combinations(start,2):
    start_sum+=stat[com[0]][com[1]]
    start_sum+=stat[com[1]][com[0]]
  for com in combinations(link,2):
    link_sum+=stat[com[0]][com[1]]
    link_sum+=stat[com[1]][com[0]]
  answer=min(answer,abs(start_sum-link_sum))
print(answer)