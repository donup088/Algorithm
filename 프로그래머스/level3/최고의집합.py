def solution(n, s):
    answer = []
    if s<n:
        return [-1]
    a=s//n
    b=s%n
    for _ in range(n):
        answer.append(a)
    for i in range(b):
        answer[i%n]+=1
    answer.sort()
    return answer