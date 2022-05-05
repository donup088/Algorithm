def solution(a):
    n=len(a)
    answer = n
    left_min=[1e9]*n
    left_min[0]=a[0]
    for i in range(1,n):
        left_min[i]=min(a[i],left_min[i-1])
        
    right_min=[1e9]*n
    right_min[-1]=a[-1]
    for i in range(n-2,-1,-1):
        right_min[i]=min(right_min[i+1],a[i])
        
    for i in range(n):
        if left_min[i]<a[i] and right_min[i]<a[i]:
            answer-=1
    return answer