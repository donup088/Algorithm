def solution(id_list, report, k):
    answer = [int(0)]*len(id_list)
    report=set(report)
    report=list(report)
    
    d=dict()
    stop=[]
    reports = {id: [] for id in id_list}
    for i in range(len(report)):
        re=report[i].split()
        a,b=re[0],re[1]
        if d.get(b)==None:
            d[b]=1
        else:
            d[b]+=1
        reports[a].append(b)
        
    for x in d.keys():
        if d[x]>=k:
             stop.append(x)
                
    for key, value in reports.items():
        for s in stop:
            if s in value:
                answer[id_list.index(key)] += 1
     
    return answer