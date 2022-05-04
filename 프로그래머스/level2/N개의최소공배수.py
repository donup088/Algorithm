import math

def lcm(a,b):
    return (a * b) // math.gcd(a,b)

def solution(arr):
    tmp=arr[0]
    for i in range(1,len(arr)):
        tmp=lcm(tmp,arr[i])
    return tmp