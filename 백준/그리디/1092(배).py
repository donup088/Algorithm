n=int(input())
c=list(map(int,input().split()))
m=int(input())
box=list(map(int,input().split()))
c.sort(reverse=True)
box.sort(reverse=True)
answer=0

if box[0]>c[0]:
  print(-1)
  exit()
else:
  while box:
    if not box:
      break
    for cr in c:
      for b in box:
        if cr>=b:
          box.remove(b)
          break
    answer+=1

print(answer)