from collections import deque

def solution(n, edge):
    answer = 0
    graph = [[] for _ in range(n + 1)]
    dis = [-1] * (n + 1)
    for e in edge:
        graph[e[0]].append(e[1])
        graph[e[1]].append(e[0])
    q = deque()
    q.append(1)
    dis[1] = 0
    while q:
        now = q.popleft()
        for i in graph[now]:
            if dis[i] == -1:
                q.append(i)
                dis[i] = dis[now] + 1

    for d in dis:
        if d == max(dis):
            answer += 1
    return answer