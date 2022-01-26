import heapq

def dijkstra(distance,graph):
    heap=[]
    heapq.heappush(heap,[0,1])
    distance[1]=0
    while heap:
        dist,now=heapq.heappop(heap)
        ## 이미 방문했던 것 지나가기
        if distance[now]<dist:
            continue
        ## 인접행렬을 통해 각각 위치에서 최소 거리를 구하고 heapq에 넣기
        for c,n in graph[now]:
            if dist+c<distance[n]:
                distance[n]=dist+c
                heapq.heappush(heap,[dist+c,n])

def solution(N, road, K):
    distance=[1e9]*(N+1)
    graph=[[] for _ in range(N+1)]
    
    ## 인접행렬 만들기 r[0] 에서 r[1] 으로 가는 비용이 r[2]
    for r in road:
        graph[r[0]].append([r[2],r[1]])
        graph[r[1]].append([r[2],r[0]])
        
    dijkstra(distance,graph)
    
    return len([x for x in distance if x<=K])