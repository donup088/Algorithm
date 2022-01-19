def solution(nums):
    answer = 0
    n = len(nums) // 2
    temp = list(set(nums))
    
    for value in temp :
        if(answer < n):
            answer +=1
            
    return answer