def solution(enroll, referral, seller, amount):
    answer=[0] * len(enroll)
    idx={}
    for i in range(len(enroll)):
        idx[enroll[i]]=i
    for i,name in enumerate(seller):
        price=100*amount[i]
        answer[idx[name]]+=price
        while referral[idx[name]]!='-':
            answer[idx[name]]-=price//10
            name=referral[idx[name]]
            answer[idx[name]]+=price//10
            price=price//10
            if price==0:
                break
        answer[idx[name]]-=price//10
    return answer