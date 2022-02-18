stack=[]
s=input()
answer=0
for i in range(len(s)):
  if s[i]=='(':
    stack.append(s[i])
  elif s[i]==')':
    stack.pop()
    if s[i-1]=='(':
      answer+=len(stack)
    else:
      answer+=1
print(answer)