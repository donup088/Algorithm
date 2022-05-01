from collections import defaultdict

def solution(n, results):
    answer = 0
    win_d=defaultdict(set)
    lose_d=defaultdict(set)
    for w,l in results:
        win_d[l].add(w)
        lose_d[w].add(l)
    
    for i in range(1,n+1):
        for w in win_d[i]:
            lose_d[w].update(lose_d[i])
        for l in lose_d[i]:
            win_d[l].update(win_d[i])

    for i in range(1,n+1):
        if len(lose_d[i])+len(win_d[i])==n-1:
            answer+=1
    
    return answer