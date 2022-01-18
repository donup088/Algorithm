def solution(board, moves):
    answer = 0
    stack_box=[]
    for i in range(len(moves)):
        for j in range(len(board[0])):
            if board[j][moves[i]-1]!=0:
                if len(stack_box)>0:
                    n=stack_box.pop()
                    if n==board[j][moves[i]-1]:
                        answer+=2
                    else:
                        stack_box.append(n)
                        stack_box.append(board[j][moves[i]-1])
                else:
                    stack_box.append(board[j][moves[i]-1])
                board[j][moves[i]-1]=0
                break
                
    return answer