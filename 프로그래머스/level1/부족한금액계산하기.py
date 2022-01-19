def solution(price, money, count):
    answer = 0
    for i in range(1,count+1):
        money-=i*price
    answer=money
    if answer>0:
        answer=0
    else:
        answer=abs(money)
    return answer