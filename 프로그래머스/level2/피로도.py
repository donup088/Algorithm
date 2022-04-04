from itertools import permutations

def solution(k, dungeons):
    answer=[]
    l=len(dungeons)
    num=[i for i in range(l)]
    pers=list(permutations(num,l))
    
    for per in pers:
        tmp=k
        cnt=0
        for p in per:
            if dungeons[p][0]<=tmp:
                tmp-=dungeons[p][1]
                cnt+=1
        answer.append(cnt)
    
    return max(answer)