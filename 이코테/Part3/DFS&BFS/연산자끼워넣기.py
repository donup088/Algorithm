import sys

sys.stdin = open("input.txt", "r")

n = int(input())
data = list(map(int, input().split()))
add, minus, mul, div = map(int, input().split())
minRes = 2147000000
maxRes = -2147000000

def dfs(i, now):
    global minRes, maxRes, add, minus, mul, div
    if i == n:
        minRes = min(minRes, now)
        maxRes = max(maxRes, now)
    else:
        if add > 0:
            add -= 1
            dfs(i + 1, now + data[i])
            add += 1
        if minus > 0:
            minus -= 1
            dfs(i + 1, now - data[i])
            minus += 1
        if mul > 0:
            mul -= 1
            dfs(i + 1, now * data[i])
            mul += 1
        if div > 0:
            div -= 1
            dfs(i + 1, int(now / data[i]))
            div += 1

dfs(1, data[0])
print(maxRes)
print(minRes)
