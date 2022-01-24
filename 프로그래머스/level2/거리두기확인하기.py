from collections import deque

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def bfs(place):
    p = []
    for i in range(5):
        for j in range(5):
            if place[i][j] == 'P':
                p.append([i, j])
    for i in p:
        q = deque([i])
        visited = [[0] * 5 for _ in range(5)]
        distance = [[0] * 5 for _ in range(5)]
        visited[q[0][0]][q[0][1]] = 1
        while q:
            y, x = q.popleft()
            for j in range(4):
                xx = x + dx[j]
                yy = y + dy[j]
                if 0 <= xx < 5 and 0 <= yy < 5 and visited[yy][xx] == 0:
                    if place[yy][xx] == 'O':
                        q.append([yy, xx])
                        visited[yy][xx] = 1
                        distance[yy][xx] = distance[y][x] + 1
                    elif place[yy][xx] == 'P' and distance[y][x] <= 1:
                        return 0
    return 1


def solution(places):
    answer = []
    for p in places:
        answer.append(bfs(p))
    return answer