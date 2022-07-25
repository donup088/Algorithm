import sys
input = sys.stdin.readline


def dfs(start, next, value, visited):
    global answer

    if len(visited) == n:
        if t[next][start] != 0:
            answer = min(answer, t[next][start] + value)

    for i in range(n):
        if t[next][i] != 0 and i != start and i not in visited:
            visited.append(i)
            dfs(start, i, value + t[next][i], visited)
            visited.pop()


n = int(input())
t = [list(map(int, input().split())) for _ in range(n)]

answer = 1e9

for i in range(n):
    dfs(i, i, 0, [i])

print(answer)
