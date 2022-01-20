def solution(s):
    answer = True
    cnt_p=0
    cnt_y=0
    s=s.upper()
    for i in s:
        if i=='P':
            cnt_p+=1
        elif i=='Y':
            cnt_y+=1
    if cnt_p!=cnt_y:
        answer=False
    

    return answer