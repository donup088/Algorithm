def solution(land, P, Q):
    arr=[]
    for l in land:
        arr+=l
    arr.sort()
    n=len(arr)
    cost=(sum(arr)-arr[0]*n)*Q
    answer=cost
    
    for i in range(1,n):
        if arr[i]!=arr[i-1]:
            diff=arr[i]-arr[i-1]
            cost=cost+diff*i*P-diff*(n-i)*Q
            if answer<cost:
                break
            answer=min(answer,cost)
    return answer