def solution(numbers):
    answer = []
    for i in range(len(numbers)):
        for j in range(i+1,len(numbers)):
            _sum=numbers[i]+numbers[j]
            if _sum not in answer:
                answer.append(_sum)
    answer.sort()
    
    return answer