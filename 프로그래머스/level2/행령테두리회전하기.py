def solution(rows, columns, queries):
    answer = []
    data=[[0]*columns for _ in range(rows)]
    num=1
    for i in range(rows):
        for j in range(columns):
            data[i][j]=num
            num+=1
    for a,b,c,d in queries:
        top, left, bottom, right = a - 1, b - 1, c - 1, d - 1    
        temp = data[top][left] 
        _min=data[top][left] 
        # 아래 -> 위
        for k in range(top, bottom):    
            data[k][left] = data[k + 1][left]
            _min=min(_min,data[k+1][left])
        # 오른쪽 -> 왼쪽
        for k in range(left, right):    
            data[bottom][k] = data[bottom][k + 1] 
            _min=min(_min,data[bottom][k + 1])
        # 위 -> 아래
        for k in range(bottom, top, -1):    
            data[k][right] = data[k - 1][right]
            _min=min(_min,data[k - 1][right])
        # 왼쪽 -> 오른쪽
        for k in range(right, left, -1):    
            data[top][k] = data[top][k - 1]
            _min=min(_min,data[top][k - 1])
        data[top][left + 1] = temp    
        
        answer.append(_min)
    
    return answer