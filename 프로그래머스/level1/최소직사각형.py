def solution(sizes):
    answer = 0
    _max=0
    _max2=0
    tmp=0
    for i in range(len(sizes)):
        for j in range(2):
            if _max<sizes[i][j]:
                _max=sizes[i][j]
                tmp=j
    for i in range(len(sizes)):
        if tmp==0:
            if sizes[i][0]<sizes[i][1]:
                sizes[i][0],sizes[i][1]=sizes[i][1],sizes[i][0]
            _max2=max(_max2,sizes[i][1])
        elif tmp==1:
            if sizes[i][1]<sizes[i][0]:
                sizes[i][0],sizes[i][1]=sizes[i][1],sizes[i][0]
            _max2=max(_max2,sizes[i][0])
    answer=_max*_max2
    return answer