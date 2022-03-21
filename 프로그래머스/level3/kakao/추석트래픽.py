def get_time(s):
    hour = int(s[:2]) * 3600
    minute = int(s[3:5]) * 60
    second = int(s[6:8])
    ms = int(s[9:])
    return (hour + minute + second) * 1000 + ms


def get_start_time(t, d):
    time = int(float(d[:-1]) * 1000)
    return get_time(t) - time + 1


def solution(lines):
    answer = 0
    start_time = []
    end_time = []
    for l in lines:
        s = l.split(' ')
        start_time.append(get_start_time(s[1], s[2]))
        end_time.append(get_time(s[1]))
    for i in range(len(lines)):
        cnt = 0
        cur_end_time = end_time[i]
        for j in range(i, len(lines)):
            if cur_end_time > start_time[j] - 1000:
                cnt += 1
        answer = max(answer, cnt)
    return answer