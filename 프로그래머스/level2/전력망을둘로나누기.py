from collections import deque


def bfs(start, visited, graph):
    q = deque()
    q.append(start)
    count = 1
    visited[start]=1
    while q:
        now = q.popleft()
        for x in graph[now]:
            if visited[x] == 0:
                visited[x] = 1
                q.append(x)
                count += 1
    return count


def solution(n, wires):
    answer = 1e9
    graph = [[] for _ in range(n + 1)]
    for s, e in wires:
        graph[s].append(e)
        graph[e].append(s)

    for s, not_visited in wires:
        visited = [0] * (n + 1)
        visited[not_visited] = 1
        count = bfs(s, visited, graph)

        answer = min(answer, abs(count - (n - count)))

    return answer