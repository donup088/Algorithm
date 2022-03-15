def solution(triangle):
    for i in range(1,len(triangle)):
        for j in range(i+1):
            # 가장 왼쪽 
            if j==0:
                triangle[i][j]+=triangle[i-1][j]
            # 가장 오른쪽
            elif j==i:
                triangle[i][j]+=triangle[i-1][j-1]
            # 가운데
            else:
                triangle[i][j]+=max(triangle[i-1][j],triangle[i-1][j-1])
    return max(triangle[-1])