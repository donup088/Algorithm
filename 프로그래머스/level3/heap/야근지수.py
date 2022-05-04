import heapq

def solution(n, works):
    answer = 0
    hq=[]
    for work in works:
        heapq.heappush(hq,(-work,work))
    while True:
        if n==0:
            break
        work=heapq.heappop(hq)[1]-1
        heapq.heappush(hq,(-work,work))
        n-=1
    
    for v in hq:
        if v[1]>0:
            answer+=v[1]**2
    return answer