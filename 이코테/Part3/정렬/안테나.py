import sys
sys.stdin = open("input.txt", "r")

n=int(input())
data=list(map(int,input().split()))
data.sort()
print(data[(n-1)//2])