answer=0
def dfs(idx,_sum,numbers,target):
    global answer
    if idx==len(numbers):
        if _sum==target:
            answer+=1
        return 
    dfs(idx+1,_sum+numbers[idx],numbers,target)
    dfs(idx+1,_sum-numbers[idx],numbers,target)

def solution(numbers, target):
    global answer
    dfs(0,0,numbers,target)
    return answer