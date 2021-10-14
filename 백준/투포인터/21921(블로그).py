n,x=map(int,input().split())
day=list(map(int,input().split()))

if max(day)==0:
  print('SAD')
else:
  count=1
  value=sum(day[:x])
  max_value=value
  for i in range(x,n):
    value+=day[i]
    value-=day[i-x]

    if value>max_value:
      max_value=value
      count=1
    elif value==max_value:
      count+=1

  print(max_value)
  print(count)