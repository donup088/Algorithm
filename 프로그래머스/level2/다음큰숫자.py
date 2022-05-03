def solution(n):
    answer = 0
    binary_n = list(map(int,format(n, 'b')))
    count=binary_n.count(1)
    num=n+1
    while True:
        binary_num=list(map(int,format(num, 'b')))
        num_count=binary_num.count(1)
        if count==num_count:
            answer=num
            break
        num+=1
    return answer