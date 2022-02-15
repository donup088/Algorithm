def solution(n, stations, w):
    answer=0
    dis=[]
    
    for i in range(1,len(stations)):
        dis.append((stations[i]-w-1)-(stations[i-1]+w))
    
    dis.append(stations[0]-w-1)
    dis.append(n-(stations[-1]+w))
    
    for d in dis:
        if d<=0:
            continue
        a=d//(2*w+1)
        b=d%(2*w+1)
        if b>0:
            answer+=a+1
        else:
            answer+=a
    return answer