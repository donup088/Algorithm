def solution(N, stages):
    answer = []
    res = []
    total = len(stages)
    for i in range(N):
        f = 0
        cnt = 0
        for j in range(len(stages)):
            if (i+1) == stages[j]:
                cnt += 1
        if total==0:
            f=0
        else:
            f = cnt / total
        res.append((i + 1, f))
        total -= cnt
    res.sort(key=lambda x: -x[1])
    for x in res:
        answer.append(x[0])
    return answer

