def solution(distance, rocks, n):
    answer = 0
    left=0
    right=distance
    
    rocks.sort()
    
    while left<=right:
        count=0
        mid=(left+right)//2 # 거리의 최솟값
        cur=0
        for rock in rocks:
            if rock-cur<mid:
                count+=1
            else:
                cur=rock
        if count>n:
            right=mid-1
        else:
            left=mid+1
            answer=mid
    return answer