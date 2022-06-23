import sys
input = sys.stdin.readline

n,k=map(int,input().split())

def check(num):
    plus=0
    while True:
        a=num//2
        b=num%2
        plus+=b
        num=a
        if num==0:
            break
    return plus

if k>=n:
    print(0)
else:
    i = n
    while True:
        if check(i)<=k:
            print(i-n)
            break
        else:
            i+=1