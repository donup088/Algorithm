def possible(answer):
    for x,y,st in answer:
        if st==0:
            if y==0 or [x-1,y,1] in answer or [x,y,1] in answer or [x,y-1,0] in answer:
                continue
            return False
        elif st==1:
            if [x,y-1,0] in answer or [x+1,y-1,0] in answer or ([x-1,y,1] in answer and [x+1,y,1] in answer):
                continue
            return False
    return True

def solution(n, build_frame):
    answer = []
    for frame in build_frame:
        x,y,st,oper=frame
        if oper == 0 :
            answer.remove([x,y,st])
            if not possible(answer):
                answer.append([x,y,st])
        if oper == 1:
            answer.append([x,y,st])
            if not possible(answer):
                answer.remove([x,y,st])            
    return sorted(answer)