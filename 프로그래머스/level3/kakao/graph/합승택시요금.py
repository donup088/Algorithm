# 플로이드 워셜 사용
def solution(n, s, a, b, fares):
    answer = 1e9
    cost=[[1e9]*(n+1) for _ in range(n+1)]
    for i,j,c in fares:
        cost[i][j]=c
        cost[j][i]=c
    for k in range(1,n+1):
        for i in range(1,n+1):
            for j in range(1,n+1):
                if i==j:
                    cost[i][j]=0
                else:
                    cost[i][j]=min(cost[i][j],cost[i][k]+cost[k][j])
    for i in range(1,n+1):
        answer=min(cost[s][i]+cost[i][a]+cost[i][b],answer)
    return answer

# 다익스트라 사용
import heapq

def solution(n, s, a, b, fares):
    def dijskstra(start):
        distance = [1e9] * (n + 1)
        distance[start] = 0
        q = []
        heapq.heappush(q, (distance[start], start))
        while q:
            dist, now = heapq.heappop(q)
            if distance[now] < dist:
                continue
            for i in graph[now]:
                cost = dist + i[1]
                if cost < distance[i[0]]:
                    distance[i[0]] = cost
                    heapq.heappush(q, (cost, i[0]))
        return distance

    answer = 1e9
    graph = [[] for _ in range(n + 1)]
    for i, j, c in fares:
        graph[i].append((j, c))
        graph[j].append((i, c))
    dist = [[]]
    for i in range(1, n + 1):
        dist.append(dijskstra(i))
    for i in range(1, n + 1):
        answer = min(answer, dist[s][i] + dist[i][a] + dist[i][b])
    return answer
