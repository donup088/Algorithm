def solution(brown, yellow):
    answer = []
    x,y=0,0
    
    for i in range(1,yellow+1):
        if yellow%i ==0:
            x=int(yellow/i)
            y=i
            if x*2+y*2+4==brown:
                answer.append(x+2)
                answer.append(y+2)
                answer.sort(reverse=True)
                return answer
    return answer