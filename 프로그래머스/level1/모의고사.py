def solution(answers):
    answer = []
    n=len(answers)
    ok=[0,0,0]
    one=[1,2,3,4,5]
    two=[2,1,2,3,2,4,2,5]
    three=[3,3,1,1,2,2,4,4,5,5]
    for i in range(n):
        if answers[i] == one[i%5]:
            ok[0]+=1
    for i in range(n):
        if answers[i] == two[i%8]:
            ok[1]+=1
    for i in range(n):
        if answers[i] == three[i%10]:
            ok[2]+=1
    m=max(ok)
    for i in range(len(ok)):
        if ok[i]==m:
            answer.append(i+1)
    return answer