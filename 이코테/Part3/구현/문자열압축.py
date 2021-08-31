def solution(s):
    answer = 1001
    for i in range(1,len(s)//2+2):
        res=""
        prev=s[:i]
        count=1
        for j in range(i,len(s),i):
            if prev==s[j:j+i]:
                count+=1
            else:
                if count==1:
                    res+=prev
                else:
                    res+=str(count)+prev
                prev=s[j:j+i]
                count=1
        if count==1:
            res+=prev
        else:
            res+=str(count)+prev
        answer=min(len(res),answer)
    return answer