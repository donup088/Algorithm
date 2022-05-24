n, m = map(int, input().split())

board = [list(map(int, input().split())) for _ in range(n)]
check = list([0] * m for _ in range(n))

t_board = [[(0, 0), (0, 1), (0, 2), (1, 1)], [(0, 1), (1, 0), (1, 1), (1, 2)],
           [(1, 0), (0, 1), (1, 1), (2, 1)], [(0, 0), (1, 0), (2, 0), (1, 1)]]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

answer = 0

def dfs(x, y, val, depth):
    global answer
    if depth == 4:
        answer = max(answer, val)
        return
    for i in range(4):
        xx = x + dx[i]
        yy = y + dy[i]
        if 0 <= xx < n and 0 <= yy < m and check[xx][yy] == 0:
            check[xx][yy] = 1
            dfs(xx, yy, val + board[xx][yy], depth + 1)
            check[xx][yy] = 0


for i in range(n):
    for j in range(m):
        check[i][j] = 1
        dfs(i, j, board[i][j], 1)
        check[i][j] = 0
        for k in range(4):
            t_answer = 0
            for l in range(4):
                kk = i + t_board[k][l][0]
                ll = j + t_board[k][l][1]
                if 0 <= kk < n and 0 <= ll < m:
                    t_answer += board[kk][ll]
            else:
              answer = max(answer, t_answer)

print(answer)
