import sys

sys.stdin = open("input.txt", "r")

def binary_search(store, target, start, end):
    if start > end:
        return
    mid = (start + end) // 2
    if store[mid] == target:
        return True
    elif store[mid] > target:
        return binary_search(store, target, start, mid - 1)
    else:
        return binary_search(store, target, mid + 1, end)


n = int(input())
store = list(map(int, input().split()))
m = int(input())
customer = list(map(int, input().split()))
res = []
customer.sort()

for i in customer:
    if binary_search(store, i, 0, len(store) - 1):
        res.append('yes')
    else:
        res.append('no')

for result in res:
    print(result, end=' ')
