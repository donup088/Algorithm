def solution(cacheSize, cities):
    answer = 0
    cache=[]
    
    if cacheSize==0:
        return len(cities)*5
    
    for c in cities:
        c=c.upper()
        if c in cache:
            used=cache.pop(cache.index(c))
            cache.append(used)
            answer+=1
        else:
            if len(cache)<cacheSize:
                cache.append(c)
            else:
                cache=cache[1:]+[c]
            answer+=5
    return answer