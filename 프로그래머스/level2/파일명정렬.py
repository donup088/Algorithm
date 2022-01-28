def solution(files):
    answer = []
    for file in files:
        head,number,tail='','',''
        flag=0
        for i in range(len(file)):
            if file[i].isdigit():
                number+=file[i]
                flag=1
            elif flag==0:
                head+=file[i]
            else:
                tail=file[i:]
                break
        answer.append((head,number,tail))
    answer=sorted(answer,key=lambda x:(x[0].lower(),int(x[1])))
    return [''.join(a) for a in answer]