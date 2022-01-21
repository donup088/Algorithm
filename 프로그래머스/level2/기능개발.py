from collections import deque

def solution(progresses, speeds):
    answer = []
    days=deque()
    for i in range(len(progresses)):
        work=100-progresses[i]
        tmp=work//speeds[i]
        if tmp*speeds[i]==work:
            days.append(tmp)
        else:
            days.append(tmp+1)
    
    while days:
        d=days.popleft()
        cnt=1
        while days:            
            d2=days.popleft()
            if d>=d2:
                cnt+=1
            else:
                days.insert(0,d2)
                break
        answer.append(cnt)
            
    return answer