import sys

input = sys.stdin.readline

n=int(input())

for _ in range(n):
    str = input().rstrip()
    left, right = [], []
    for s in str:
        if s == '<':
            if left:
                right.append(left.pop())
        elif s == '>':
            if right:
                left.append(right.pop())
        elif s == '-':
            if left:
                left.pop()
        else:
            left.append(s)
    left.extend(reversed(right))
    print(''.join(left))