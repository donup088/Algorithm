def solution(msg):
    answer = []
    d = {chr(i + 64): i for i in range(1, 27)}
    tmp=''
    l=len(d)
    i=0
    while i<len(msg):
        tmp+=msg[i]
        if tmp in d.keys():
            i+=1
            continue
        else:
            l+=1
            d[tmp]=l
            answer.append(d[tmp[:-1]])
            tmp=''
            
        
    answer.append(d[tmp])
    return answer