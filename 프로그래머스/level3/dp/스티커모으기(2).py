def solution(sticker):
    answer=0
    if len(sticker)==1:
        return sticker[0]
    #첫번째 스티커 선택
    dp=[0]*len(sticker)
    dp[0]=sticker[0]
    dp[1]=dp[0]
    for i in range(2,len(sticker)-1):
        dp[i]=max(dp[i-1],dp[i-2]+sticker[i])
    answer=max(dp)
    
    #첫번째 스티커 선택 x
    dp=[0]*len(sticker)
    dp[0]=0
    dp[1]=sticker[1]
    for i in range(2,len(sticker)):
        dp[i]=max(dp[i-1],dp[i-2]+sticker[i])
    return max(answer,max(dp))