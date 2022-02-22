import math 

def change_n(n, q):
    rev_base = ''

    while n > 0:
        n, mod = divmod(n, q)
        rev_base += str(mod)

    return rev_base[::-1] 

def is_prime_number(x):
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False 
    return True 

def solution(n, k):
    answer=0
    tmp=change_n(n,k)
    t=tmp.split('0')
    for i in t:
        if i !='':
            if int(i)>1:
                if is_prime_number(int(i)):
                    answer+=1
    return answer