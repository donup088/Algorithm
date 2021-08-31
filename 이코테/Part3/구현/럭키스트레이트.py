import sys

sys.stdin=open("input.txt","r")

n=input()
lsum=sum(map(int,n[:len(n)//2]))
rsum=sum(map(int,n[len(n)//2:]))
if lsum==rsum:
  print('LUCKY')
else:
  print('READY')

