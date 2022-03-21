def get_time(s):
    time = s.split(':')
    return int(time[0]) * 60 + int(time[1])


def to_time(t):
    hour = t // 60
    minute = t % 60
    if hour < 10:
        hour = '0' + str(hour)
    if minute < 10:
        minute = '0' + str(minute)
    return str(hour) + ':' + str(minute)


def solution(n, t, m, timetable):
    answer = 0
    time = []
    for tt in timetable:
        time.append(get_time(tt))
    time.sort()
    bus = [9 * 60 + t * i for i in range(n)]
    i = 0
    for bt in bus:
        cnt = 0
        while cnt < m and i < len(time) and time[i] <= bt:
            cnt += 1
            i += 1
        if cnt < m:
            answer = bt
        else:
            answer = time[i - 1] - 1
    answer = to_time(answer)
    return answer