import string

tmp = string.digits+string.ascii_uppercase
def convert(num, base) :
    q, r = divmod(num, base)
    if q == 0 :
        return tmp[r] 
    else :
        return convert(q, base) + tmp[r]

def solution(n, t, m, p):
    answer = ''
    idx=0
    count=0
    seq=1
    while True:        
        num=convert(idx,n)
        for s in num:
            if count==t:
                return answer
            seq=seq%(m+1)
            if seq==0:
                seq=1
            if seq==p:
                count+=1
                answer+=s
            seq+=1
        idx+=1