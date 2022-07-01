import sys
from itertools import combinations

input = sys.stdin.readline

def back(round):
    global ans
    if round == 15:
        ans = 1
        for r in res:
            if r.count(0) != 3:
                ans = 0
                break
        return
    team1, team2 = game[round]
    for x, y in ((0, 2), (1, 1), (2, 0)):
        if res[team1][x] > 0 and res[team2][y] > 0:
            res[team1][x] -= 1
            res[team2][y] -= 1
            back(round + 1)
            res[team1][x] += 1
            res[team2][y] += 1

answer = []
game = list(combinations(range(6), 2))
for _ in range(4):
    data = list(map(int, input().split()))
    res = [data[i:i + 3] for i in range(0, 16, 3)]
    print(res)
    ans = 0
    back(0)
    answer.append(ans)

print(*answer)