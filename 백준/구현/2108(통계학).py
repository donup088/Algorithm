import sys
from collections import Counter

input = sys.stdin.readline

data=[]
n=int(input())
for _ in range(n):
  num=int(input())
  data.append(num)

data.sort()
most=0
counter=Counter(data).most_common()
if len(counter)>1 and counter[0][1]==counter[1][1]:
  most=counter[1][0]
else:
  most=counter[0][0]
print(round(sum(data)/n))
print(data[n//2])
print(most)
print(max(data)-min(data))  