def solution(m, n, board):
    answer = 0
    # m 은 세로 n 은 가로
    for i in range(m):
        board[i] = list(board[i])
    while True:
        del_set=set()
        for i in range(m-1):
            for j in range(n-1):
                if board[i][j]==0:
                    continue
                if board[i][j]==board[i][j+1] and board[i][j]==board[i+1][j] and board[i][j]==board[i+1][j+1]:
                    del_set.add((i,j))
                    del_set.add((i+1,j))
                    del_set.add((i,j+1))
                    del_set.add((i+1,j+1))
        if len(del_set)>0:
            answer+=len(del_set)
            for i,j in del_set:
                board[i][j]=0

        else:
            break
        
        while True:
            moved=0
            for i in range(m-1):
                for j in range(n):
                    if board[i][j]!=0 and board[i+1][j]==0:
                        board[i+1][j]=board[i][j]
                        board[i][j]=0
                        moved=1
            if moved==0:
                break
    return answer