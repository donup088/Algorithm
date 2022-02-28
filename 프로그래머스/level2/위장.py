def solution(clothes):
    answer = 1
    d={}
    for name, category in clothes:
        if d.get(category)!=None:
            d[category].append(name)
        else:
            l=[]
            l.append(name)
            d[category]=l
    
    for key,value in d.items():
        answer=answer*(len(value)+1)
    
    return answer-1