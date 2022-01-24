def solution(str1, str2):
    answer = 0
    str1_tmp=[]
    str2_tmp=[]
    for i in range(len(str1)-1):
        if str1[i].isalpha() and str1[i+1].isalpha():
            str1_tmp.append(''.join(str1[i]+str1[i+1]).upper())
    for i in range(len(str2)-1):
        if str2[i].isalpha() and str2[i+1].isalpha():
            str2_tmp.append(''.join(str2[i]+str2[i+1]).upper())
    
    ins=set(str1_tmp) & set(str2_tmp)
    union=set(str1_tmp)|set(str2_tmp)
    
    if len(union)==0:
        answer=1*65536
    else:
        ins_sum=sum([min(str1_tmp.count(i),str2_tmp.count(i)) for i in ins])
        union_sum=sum([max(str1_tmp.count(i),str2_tmp.count(i)) for i in union])
        answer=int(ins_sum/union_sum*65536)
    return answer
