import sys
from collections import deque

sys.stdin = open("input.txt", "r")

n, l, r = map(int, input().split())
data = []
for _ in range(n):
    data.append(list(map(int, input().split())))

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def process(x, y):
    united = []
    united.append((x, y))
    q = deque()
    q.append((x, y))
    summary = data[x][y]
    unionCount = 1
    union[x][y] = 1
    while q:
        x, y = q.popleft()
        for i in range(4):
            xx = x + dx[i]
            yy = y + dy[i]
            if 0 <= xx < n and 0 <= yy < n and union[xx][yy] == -1:
                if l <= abs(data[xx][yy] - data[x][y]) <= r:
                    q.append((xx, yy))
                    union[xx][yy] = 1
                    summary += data[xx][yy]
                    unionCount += 1
                    united.append((xx, yy))
    for a, b in united:
        data[a][b] = summary // unionCount
    
result = 0

while True:
    union = [[-1] * n for _ in range(n)]
    index = 0
    for i in range(n):
        for j in range(n):
            if union[i][j] == -1:
                process(i, j)
                index += 1
    if index == n * n:
        break
    result += 1
print(result)
