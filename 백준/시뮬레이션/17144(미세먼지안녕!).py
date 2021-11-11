def spread():
    tmp_arr = [[0] * C for _ in range(R)]
    for i in range(R):
        for j in range(C):
            if room[i][j] != 0 and room[i][j] != -1:
                tmp = 0
                for k in range(4):
                    xx = dx[k] + i
                    yy = dy[k] + j
                    if 0 <= xx < R and 0 <= yy < C and room[xx][yy] != -1:
                        tmp_arr[xx][yy] += room[i][j] // 5
                        tmp += room[i][j] // 5
                room[i][j] -= tmp

    for i in range(R):
        for j in range(C):
            room[i][j] += tmp_arr[i][j]


def air():
    y, x = cleaner[0]

    temp = room[y][C - 1]
    for i in range(C - 1, 1, -1):
        room[y][i] = room[y][i - 1]
    room[y][1] = 0

    temp2 = room[0][C - 1]
    for i in range(y - 1):
        room[i][C - 1] = room[i + 1][C - 1]
    room[y - 1][C - 1] = temp

    temp = room[0][0]
    for i in range(C - 2):
        room[0][i] = room[0][i + 1]
    room[0][C - 2] = temp2

    for i in range(y - 1, 1, -1):
        room[i][0] = room[i - 1][0]
    room[1][0]=temp

    y2, x2 = cleaner[1]

    temp = room[y2][C - 1]
    for i in range(C - 1, 1, -1):
        room[y2][i] = room[y2][i - 1]
    room[y2][1] = 0

    temp2 = room[R - 1][C - 1]
    for i in range(R - 1, y2 + 1, -1):
        room[i][C - 1] = room[i - 1][C - 1]
    room[y2 + 1][C - 1] = temp

    temp = room[R - 1][0]
    for i in range(C - 2):
        room[R - 1][i] = room[R - 1][i + 1]
    room[R - 1][C - 2] = temp2

    for i in range(y2 + 1, R - 1):
        room[i][0] = room[i + 1][0]
    room[R - 2][0] = temp

room = []
cleaner = []
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]
R, C, T = map(int, input().split())
for _ in range(R):
    room.append(list(map(int, input().split())))
for i in range(R):
    for j in range(C):
        if room[i][j] == -1:
            cleaner.append((i, j))
       

for i in range(T):
    spread()
    air()

res = 0
for i in range(R):
    for j in range(C):
        if room[i][j] > 0:
            res += room[i][j]
print(res)