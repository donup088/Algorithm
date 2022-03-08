def DFS(n,cur,computers,visited):
    visited[cur]=1
    for c in range(n):
        if c!=cur and computers[cur][c]==1:
            if visited[c]==0:
                DFS(n,c,computers,visited)

def solution(n, computers):
    visited=[0]*n
    answer=0
    for i in range(n):
        if visited[i]==0:
            DFS(n,i,computers,visited)
            answer+=1
    return answer