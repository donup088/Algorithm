def solution(N, stages):
    answer = []
    fail=[]
    total=len(stages)
    for i in range(N): #
        cnt=stages.count(i+1)
        if cnt==0:
            fail.append((i+1,0))
        else:
            fail.append((i+1,cnt/total))
        total-=cnt        
    fail.sort(key = lambda x :(-x[1], x[0]))
    
    for f in fail:
        answer.append(f[0])    
    return answer