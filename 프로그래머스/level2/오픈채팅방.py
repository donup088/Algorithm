def solution(record):
    answer = []
    d=dict()
    for i in range(len(record)):
        s=record[i].split()
        if s[0]=="Enter" or s[0]=="Change":
            a,b,c=s
            d[b]=c    
    
    for j in range(len(record)):
        s=record[j].split()
        
        if s[0]=="Enter":
            answer.append(d[s[1]]+'님이 들어왔습니다.')
        elif s[0]=="Leave":
            answer.append(d[s[1]]+'님이 나갔습니다.')
    return answer