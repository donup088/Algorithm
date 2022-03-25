n=int(input())
data=list(map(int,input().split()))
answer=[]
l=0
r=n-1

data.sort()

diff=abs(data[l]+data[r])

while l<r:
  s_l=data[l]
  s_r=data[r]
  diff_tmp=s_l+s_r
  if abs(diff_tmp)<=diff:
    diff=abs(diff_tmp)
    answer=[s_l,s_r]
  if diff_tmp<0:
    l+=1
  else:
    r-=1

print(answer[0],answer[1])