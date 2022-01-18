def solution(new_id):
    answer = ''
    new_id=new_id.lower()
    for s in new_id:
        if s.isalnum() or s in '-_.':
            answer+=s
    while '..' in answer:
        answer= answer.replace('..','.')
    if answer[0]=='.' and len(answer)>1:
        answer=answer[1:]
    if answer[-1]=='.':
        answer=answer[:-1]
    if answer=='':
        answer='a'
    if len(answer)>=16:
        answer=answer[:15]
        if answer[-1]=='.':
            answer=answer[:-1]

    while len(answer)<3:
        answer+=answer[-1]
    return answer