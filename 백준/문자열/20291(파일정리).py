file=dict()

def get_ext(s):
  split_s=s.split('.')
  return split_s[1]

def set_count(e):
  if file.get(e)==None:
    file[e]=1
  else:
    file[e]+=1

N=int(input())

for _ in range(N):
  s=input()
  ext=get_ext(s)
  set_count(ext)

file=sorted(file.items())

for a,b in file:
  print(a,b)