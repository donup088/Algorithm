N=int(input())
s=input()
Blue=[]
Red=[]
res=1
r_group=1
b_group=1

def group_count(arr):
  count=1
  for i in range(len(arr)-1):
    tmp=arr[i][0]
    if tmp+1!=arr[i+1][0]:
      count+=1
    tmp=arr[i+1][0]
  return count

for i in range(N):
  if s[i]=='B':
    Blue.append((i,s[i]))
  else:
    Red.append((i,s[i]))

b_group=group_count(Blue)
r_group=group_count(Red)

if b_group<r_group:
  if b_group>1:
    res+=b_group
else:
  if r_group>1:
    res+=r_group

print(res)