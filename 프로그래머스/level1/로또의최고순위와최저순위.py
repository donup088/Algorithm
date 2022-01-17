def solution(lottos, win_nums):
    answer = []
    min_ans=0
    max_ans=0
    zero_count=0
    for i in range(len(lottos)):
        if lottos[i]!=0:
            if lottos[i] in win_nums:
                min_ans+=1        
        elif lottos[i]==0:
            zero_count+=1
        
    max_ans=zero_count+min_ans
    
    if 7-max_ans>=7:
        answer.append(6)
    else:
        answer.append(7-max_ans)
    if 7-min_ans>=7:
        answer.append(6)
    else:
        answer.append(7-min_ans)
    
    return answer