import math

def solution(fees, records):
    answer = []
    tmp=[]
    car=[]
    d={}
    for r in records:
        t,num,action=r.split()
        time=t.split(":")
        m=int(time[0])*60+int(time[1])
        if action=='IN':
            tmp.append((num,m))
        if action=='OUT':
            for i in range(len(tmp)):
                if tmp[i][0]==num:
                    if d.get(num)==None:
                        d[num]=m-tmp[i][1]
                    else:
                        d[num]=d[num]+m-tmp[i][1]
                    del tmp[i]
                    break
    
    for n,t in tmp:
        if d.get(n)==None:
                d[n]=(23*60+59)-t
        else:
            d[n]=d[n]+(23*60+59)-t
                
    for k,v in d.items():
        if v<=fees[0]:
            car.append((k,fees[1]))
        else:
            car.append((k,fees[1]+math.ceil((v-fees[0])/fees[2])*fees[3]))
    car.sort()
    for c in car:
        answer.append(c[1])
    return answer