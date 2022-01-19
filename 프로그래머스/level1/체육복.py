def solution(n, lost, reserve):
    r=set(reserve)-set(lost)
    l=set(lost)-set(reserve)
    answer=n-len(l)
    for i in r:
        if i-1 in l:
            l.remove(i-1)
            answer+=1
        elif i+1 in l:
            l.remove(i+1)
            answer+=1
            
    return answer