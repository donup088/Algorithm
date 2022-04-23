def solution(routes):
    answer = 1
    routes.sort(key = lambda x: x[1])
    tmp=routes[0][1]
    for i in range(1,len(routes)):
        if routes[i][0]>tmp:
            tmp=routes[i][1]
            answer+=1
    return answer