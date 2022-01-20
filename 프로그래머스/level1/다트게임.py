def solution(dartResult):
    answer = 0
    numbers=[]
    s=''
    n=0
    for d in dartResult: 
        if d.isdigit():
            s+=d
            n=int(s)
            continue
        elif d=='S':
            n=n
            numbers.append(n)
        elif d=='D':
            n=n*n
            numbers.append(n)
        elif d=='T':
            n=n*n*n
            numbers.append(n)
        elif d=='#':
            if len(numbers)>0:
                p=numbers.pop()
                p=p*(-1)
                numbers.append(p)
        elif d=='*':
            p2=numbers.pop()
            p2*=2
            if len(numbers)>0:
                p1=numbers.pop()
                p1*=2
                numbers.append(p1)
            numbers.append(p2)
        s=''
    answer=sum(numbers)
    return answer