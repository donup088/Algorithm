def find_parent(parent,x):
    if parent[x]!=x:
        parent[x]=find_parent(parent,parent[x])
    return parent[x]

def union_parent(parent,a,b):
    a=find_parent(parent,a)
    b=find_parent(parent,b)
    if a<b:
        parent[b]=a
    else:
        parent[a]=b

def solution(n, costs):
    answer = 0
    parent=[0]*n
    for i in range(n):
        parent[i]=i
    costs.sort(key=lambda x:x[2])
    
    for cost in costs:
        if find_parent(parent,cost[0])!=find_parent(parent,cost[1]):
            union_parent(parent,cost[0],cost[1])
            answer+=cost[2]
    return answer