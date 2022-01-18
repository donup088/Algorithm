from itertools import combinations

def solution(nums):
    answer=0
    n=list(combinations(nums, 3))
    
    for a,b,c in n:
        t=a+b+c
        for i in range(2,t):
            flag=1
            if t%i==0:
                flag=0
                break
        if flag:
            answer+=1
    return answer