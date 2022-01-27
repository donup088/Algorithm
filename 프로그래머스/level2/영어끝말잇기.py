def solution(n, words):
    answer = []
    history=[]
    number, order = 0,0
    last_word=words[0][-1]
    history.append(words[0])
    for i in range(1,len(words)):
        if words[i] not in history and words[i][0] == last_word:
                history.append(words[i])
                last_word = words[i][-1]
        else:
            number = (i%n)+1
            order = (i//n)+1
            break
    return [number,order]