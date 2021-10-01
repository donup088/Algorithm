def solution(str):
  global flag
  if len(str)==len(s):
    if str==s:
      flag=1
    return
    
  if str[0]=='B':
    str=str[::-1]
    str.pop()
    solution(str)
    str.append('B')
    str=str[::-1]
  if str[-1]=='A':
    str.pop()
    solution(str)
    str.append('A')
    
s=list(input())
t=list(input())
flag=0
solution(t)

if flag:
  print(1)
else:
  print(0)