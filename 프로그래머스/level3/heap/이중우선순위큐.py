import heapq

def solution(operations):
    hq=[]
    for oper in operations:
        op,n=oper.split(' ')
        if op=='I':
            heapq.heappush(hq,int(n))
        elif op=='D' and n=='1':
            if hq:
                hq = heapq.nlargest(len(hq), hq)[1:]
                heapq.heapify(hq)
        elif op=='D' and n=='-1':
            if hq:
                heapq.heappop(hq)
    _max,_min=0,0
    if hq:
        _max=max(hq)
        _min=min(hq)
    
    return [_max,_min]