def check1(s,l,r):
  while l<r:
    if s[l]==s[r]:
      l+=1
      r-=1
    else:
      return False
  return True

def check2(s,l,r):
  while l<r:
    if s[l]==s[r]:
      l+=1
      r-=1
    else:
      res1=check1(s,l+1,r)
      res2=check1(s,l,r-1)
      if res1==True or res2==True:
        return 1
      else:
        return 2
  return 0

N=int(input())
for _ in range(N):
  s=input()
  ans=check2(s,0,len(s)-1)
  print(ans)