from itertools import combinations
from collections import Counter

def solution(orders, course):
    answer = []
    for i in course:
        temp = []
        for order in orders:
            t = combinations(sorted(order), i)
            temp += t

        counter = Counter(temp).most_common()

        if len(counter) != 0 and counter[0][1] > 1:
            for m, n in counter:
                if n < counter[0][1]:
                    break

                answer.append(''.join(m))

    return sorted(answer)