def solution(n, times):
    answer = 0
    left=1
    right=max(times)*n
    
    while left<=right:
        total=0
        mid=(left+right)//2
        for t in times:
            total+=mid//t
        if total<n:
            left=mid+1
        else:
            right=mid-1
            answer=mid
        
    return answer