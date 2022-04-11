from collections import deque

def bfs(board, start):
    dx = [0, -1, 0, 1]
    dy = [-1, 0, 1, 0]
    q = deque([start])
    n = len(board)
    cost = [[1e9] * n for _ in range(n)]
    cost[0][0] = 0
    while q:
        x, y, d, v = q.popleft()
        for i in range(4):
            xx, yy = x + dx[i], y + dy[i]
            if i != d:
                n_v = v + 600
            else:
                n_v = v + 100
            if 0 <= xx < n and 0 <= yy < n and board[xx][
                    yy] == 0 and cost[xx][yy] > n_v:
                cost[xx][yy] = n_v
                q.append([xx, yy, i, n_v])
    return cost[-1][-1]


def solution(board):
    return min(bfs(board, (0, 0, 2, 0)), bfs(board, (0, 0, 3, 0)))