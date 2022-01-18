def solution(participant, completion):
    answer = ''
    d=dict()
    for s in completion:
        if d.get(s)==None:
            d[s]=1
        else:
            d[s]+=1
    for s in participant:
        if d.get(s)==None:
            answer=s
        else:
            d[s]-=1
    for k,v in d.items():
        if v==-1:
            answer=k  
    return answer