def solution(n, arr1, arr2):
    answer = []
    temp = [['#']*n for _ in range(n)]
    map1=[]
    map2=[]
    for i in range(n):
        tmp=arr1[i]
        s=''
        while tmp>=1:
            tmp, rest = divmod(tmp, 2)
            s+=str(rest)
        while len(s)<n:
            s+=str(0)
        map1.append(list(s[::-1]))
        tmp=arr2[i]
        s=''
        while tmp>=1:
            tmp, rest = divmod(tmp, 2)
            s+=str(rest)
        while len(s)<n:
            s+=str(0)
        map2.append(list(s[::-1]))
    for i in range(n):
        s=''
        for j in range(n):
            print(map1[i][j],map2[i][j])
            if map1[i][j]=='0' and map2[i][j]=='0':
                temp[i][j]=' '
            s+=temp[i][j]
        answer.append(s)
    return answer