def solution(numbers):
    answer = 0
    value=[1,2,3,4,5,6,7,8,9]
    for v in value:
        if v not in numbers:
            answer+=v
        
    return answer