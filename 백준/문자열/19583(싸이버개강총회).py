import sys
input = sys.stdin.readline

start,end,s_end=input().split()
start= int(start[:2] + start[3:])
end=int(end[:2] + end[3:])
s_end=int(s_end[:2] + s_end[3:])

attend=set()
answer=0

while True:
  try:
    time,name=input().split()
    time = int(time[:2] + time[3:])
    if time<=start:
      attend.add(name)
    elif end<=time<=s_end and name in attend:
      attend.remove(name)
      answer+=1
  except:
        break

print(answer)