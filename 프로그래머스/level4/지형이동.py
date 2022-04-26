import heapq

def solution(land, height):
    answer = 0
    n = len(land)
    visited = [[0] * n for _ in range(n)]
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    hq = [[0, 0, 0]]
    while hq:
        cost, x, y = heapq.heappop(hq)
        if visited[x][y] != 0:
            continue
        visited[x][y] = 1
        answer += cost
        for i in range(4):
            xx, yy = x + dx[i], y + dy[i]
            if 0 <= xx < n and 0 <= yy < n and visited[xx][yy] == 0:
                diff = abs(land[xx][yy] - land[x][y])
                if diff > height:
                    heapq.heappush(hq, [diff, xx, yy])
                else:
                    heapq.heappush(hq, [0, xx, yy])

    return answer