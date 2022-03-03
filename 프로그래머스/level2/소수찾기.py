from itertools import permutations
import math

def is_prime_num(n):
    for i in range(2, int(math.sqrt(n))+1): 
        if n % i == 0:
            return False

    return True

def solution(numbers):
    answer = 0
    tmp_list=[]
    for i in range(1,len(numbers)+1):
        a=list(permutations(numbers,i))
        for i in range(len(a)):
            tmp=a[i]
            s=''
            for t in tmp:
                s+=t 
            if s not in tmp_list:
                tmp_list.append(int(s))
                
    tmp_list=list(set(tmp_list))

    for t in tmp_list:
        if t>=2 and is_prime_num(t):
            answer+=1
    return answer