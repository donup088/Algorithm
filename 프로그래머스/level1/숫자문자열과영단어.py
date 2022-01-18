def solution(s):
    answer = ''
    d=dict()
    d['zero']='0'
    d['one']='1'
    d['two']='2'
    d['three']='3'
    d['four']='4'
    d['five']='5'
    d['six']='6'
    d['seven']='7'
    d['eight']='8'
    d['nine']='9'
    
    tmp=''
    for i in s:
        if i.isalpha():
            tmp+=i
            if d.get(tmp)!=None:
                answer+=d[tmp]
                tmp=''
        else:
            answer+=i
    answer=int(answer)
            
    return answer