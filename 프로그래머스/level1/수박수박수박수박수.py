def solution(n):
    answer=''
    for i in range(2,n+2):
        if i %2==0:
            answer+='수'
        else:
            answer+='박'
        
    return answer