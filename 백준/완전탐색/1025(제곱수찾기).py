def issquare(n): 
  temp = n ** 0.5 
  if int(temp) == temp:
    return True 
  else:
    return False

numbers=[]
n,m=map(int,input().split())
answer=-1

for i in range(n):
  numbers.append(list(map(int,input().rstrip())))

for i in range(n):
  for j in range(m):
    for wn in range(-n,n):
      for wm in range(-m,m):
        if wn==0 and wm==0:
          continue
        step=0
        value=''
        x=i
        y=j
        while 0<=x<n and 0<=y<m:
          step+=1
          value+=str(numbers[x][y])
          value_int=int(''.join(value))
          if issquare(value_int):
            answer=max(answer,value_int)
          x=i+step*wn
          y=j+step*wm
print(answer)