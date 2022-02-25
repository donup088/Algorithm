def solution(phone_book):
    answer = True
    d={}
    for i in range(len(phone_book)):
        d[phone_book[i]]=1
    
    for key, value in d.items():
        for i in range(len(key)):
            if d.get(key[:i]) !=None:
                return False
    return True