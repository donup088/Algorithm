from itertools import combinations_with_replacement
from collections import Counter

def solution(n, info):
    max_diff=0
    max_cnt={}
    for comb in combinations_with_replacement(range(11),n):
        cnt=Counter(comb)
        a,l=0,0
        for i in range(1,11):
            if info[10-i]<cnt[i]:
                l+=i
            elif info[10-i]>0:
                a+=i
        diff=l-a
        if diff>max_diff:
            max_diff=diff
            max_cnt=cnt
    if max_diff>0:
        answer=[0]*11
        for n in max_cnt:
            answer[10-n]=max_cnt[n]
        return answer
    return [-1]