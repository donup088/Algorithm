from collections import deque

def solution(prices):
    answer=[]
    que=deque(prices)
    while que:
        _time=0
        p=que.popleft()
        for q in que:
            _time+=1
            if q<p:
                break
        answer.append(_time)
    return answer