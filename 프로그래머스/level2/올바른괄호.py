def solution(s):
    answer = True
    stack=[]
    for word in s:
        if word=='(':
            stack.append(word)
        if word==')':
            if len(stack)==0:
                return False
            tmp=stack.pop()
            if tmp!='(':
                return False
    if len(stack)>0:
        return False
    return True