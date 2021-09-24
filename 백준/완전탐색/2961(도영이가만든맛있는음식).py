from itertools import combinations

n = int(input())
data = []
res = 1e9
for _ in range(n):
    a, b = map(int, input().split())
    data.append((a, b))
combs = []
for i in range(1, n + 1):
    combs.append(combinations(data, i))

for com in combs:
    for x in com:
        plus = 0
        mul = 1
        for a, b in x:
            mul *= a
            plus += b
        gap = abs(plus - mul)
        res = min(res, gap)
print(res)
