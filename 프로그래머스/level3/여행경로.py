from collections import defaultdict


def solution(tickets):
    answer = []
    d = defaultdict(list)

    for t in tickets:
        d[t[0]].append(t[1])

    for key in d.keys():
        d[key].sort(reverse=True)

    stack = ['ICN']
    while stack:
        tmp = stack[-1]

        if not d[tmp]:
            answer.append(stack.pop())
        else:
            stack.append(d[tmp].pop())
    answer.reverse()
    return answer