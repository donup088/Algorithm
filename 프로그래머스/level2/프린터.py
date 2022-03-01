from collections import deque

def solution(priorities, location):
    answer = 0
    q=deque()
    for i in range(len(priorities)):
        if i==location:
            q.append([priorities[i],1])
        else:
            q.append([priorities[i],0])
    while True:
        num=q.popleft()
        for i in range(len(q)):
            if num[0]<q[i][0]:
                q.append([num[0],num[1]])
                break
        else:
            answer+=1
            if num[1]==1:
                break
        
    return answer