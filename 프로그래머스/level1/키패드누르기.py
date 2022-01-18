def solution(numbers, hand):
    answer = ''
    d=dict()
    d['1']=[0,0]
    d['2']=[0,1]
    d['3']=[0,2]
    d['4']=[1,0]
    d['5']=[1,1]
    d['6']=[1,2]
    d['7']=[2,0]
    d['8']=[2,1]
    d['9']=[2,2]
    d['0']=[3,1]
    tmp_l=[3,0]
    tmp_r=[3,2]
    for n in numbers:
        if n in [1,4,7]:
            answer+='L'
            tmp_l=d[str(n)]
        elif n in [3,6,9]:
            answer+='R'
            tmp_r=d[str(n)]
        elif n in [2,5,8,0]:
            a=d[str(n)]
            d_l=abs(a[0]-tmp_l[0])+abs(a[1]-tmp_l[1])
            d_r=abs(a[0]-tmp_r[0])+abs(a[1]-tmp_r[1])
            if d_l>d_r:
                answer+='R'
                tmp_r=d[str(n)]
            elif d_l<d_r:
                answer+='L'
                tmp_l=d[str(n)]
            else:
                if hand =='left':
                    answer+='L'
                    tmp_l=d[str(n)]
                else :
                    answer+='R'
                    tmp_r=d[str(n)]
    return answer