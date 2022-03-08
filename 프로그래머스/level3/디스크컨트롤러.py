import heapq

def solution(jobs):
    answer = 0
    hq=[]
    start=-1
    now=0
    i=0
    while i<len(jobs):
        for s,t in jobs:
            if start<s<=now:
                heapq.heappush(hq,[t,s])
        if hq:
            cur=heapq.heappop(hq)
            start=now
            now+=cur[0]
            answer+=(now-cur[1])
            i+=1
        else:
            now+=1
    
    return int(answer/len(jobs))