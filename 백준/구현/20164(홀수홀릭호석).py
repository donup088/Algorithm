N=input()

max_res=0
min_res=1e9

def odd_count(n):
  s=str(n)
  odd=0
  for x in s:
    if int(x)%2!=0:
      odd+=1
  return odd


def sol(n,count):
  global max_res,min_res
  if len(n)==1:
    max_res=max(max_res,count)
    min_res=min(min_res,count)
  elif len(n)==2:
    tmp=str(int(n[0])+int(n[1]))
    sol(tmp,count+odd_count(tmp))
  else:
    for i in range(len(n)-2):
      for j in range(i+1,len(n)-1):
        a=n[:i+1]
        b=n[i+1:j+1]
        c=n[j+1:]
        tmp=str(int(a)+int(b)+int(c))
        sol(tmp,count+odd_count(tmp))

sol(N,odd_count(N))
print(min_res,max_res)