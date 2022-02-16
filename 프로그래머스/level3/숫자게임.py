def solution(A, B):
    answer=0
    A.sort(reverse=True)
    B.sort(reverse=True)
    for a in A:
        if B[0]<=a:
            continue
        else:
            B.pop(0)
            answer+=1
    return answer