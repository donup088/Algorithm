import sys
sys.stdin = open("input.txt", "r")

left={'q':(0,0),'w':(0,1),'e':(0,2),'r':(0,3),'t':(0,4),'a':(1,0),'s':(1,1),'d':(1,2),'f':(1,3),'g':(1,4),'z':(2,0),'x':(2,1),'c':(2,2),'v':(2,3)}

right={'y':(0,5),'u':(0,6),'i':(0,7),'o':(0,8),'p':(0,9),'h':(1,5),'j':(1,6),'k':(1,7),'l':(1,8),'b':(2,4),'n':(2,5),'m':(2,6)}

l,r=input().split()
s=input()
cnt=0
  
lx,ly=left[l]
rx,ry=right[r]

for i in range(len(s)):
  if s[i] in left:
    x,y=left[s[i]]
    cnt+=abs(lx-x)+abs(ly-y)+1
    lx=x
    ly=y
  else:
    x,y=right[s[i]]
    cnt+=abs(rx-x)+abs(ry-y)+1
    rx=x
    ry=y
print(cnt)