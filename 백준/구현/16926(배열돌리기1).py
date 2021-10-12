N, M, R = map(int, input().split())

board = [list(map(int, input().split())) for _ in range(N)]

for _ in range(R):
    for i in range(min(N, M) // 2):
        cx, cy = i, i
        c_value = board[cx][cy]
        for j in range(i + 1, N - i):
            cx = j
            prev_value = board[cx][cy]
            board[cx][cy] = c_value
            c_value = prev_value
        for j in range(i + 1, M - i):
            cy = j
            prev_value = board[cx][cy]
            board[cx][cy] = c_value
            c_value = prev_value
        for j in range(i + 1, N - i):
            cx = N - j - 1
            prev_value = board[cx][cy]
            board[cx][cy] = c_value
            c_value = prev_value
        for j in range(i + 1, M - i):
            cy = M - j - 1
            prev_value = board[cx][cy]
            board[cx][cy] = c_value
            c_value = prev_value
for i in range(N):
    for j in range(M):
        print(board[i][j], end=' ')
    print()
