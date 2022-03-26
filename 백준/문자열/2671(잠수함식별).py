import re

s = input()
p = re.compile('(100+1+|01)+')
m = p.fullmatch(s)
if m:
    print("SUBMARINE")
else:
    print("NOISE")