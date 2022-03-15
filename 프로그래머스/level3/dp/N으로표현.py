def solution(N, number):
    answer = -1
    dp=[[] for _ in range(9)]
    for i in range(1,9):
        dp[i].append(int(str(N)*i))
        for j in range(1,i):
            for k in dp[j]:
                for z in dp[i-j]:
                    dp[i].append(k+z)
                    dp[i].append(k-z)
                    dp[i].append(k*z)
                    if z:
                        dp[i].append(k//z)
        dp[i]=list(set(dp[i]))
        if number in dp[i]:
            answer=i
            break
    return answer