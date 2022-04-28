import sys
input = sys.stdin.readline

d={}
while True:
  tree=input().rstrip()
  if len(tree)==0:
    break
  if d.get(tree)==None:
    d[tree]=1
  else:
    d[tree]+=1
total=sum(d.values())    
d = sorted(d.items())

for key,value in d:
  print('%s %.4f' %(key,(value/total)*100))