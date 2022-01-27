def solution(skill, skill_trees):
    answer = 0
    for st in skill_trees:
        tmp=skill
        for s in st:
            if s in tmp:
                if tmp[0]!=s:
                    break
                tmp=tmp[1:]
        else:
            answer+=1
            
    return answer