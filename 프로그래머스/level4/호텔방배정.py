import sys
sys.setrecursionlimit(10000)

def find(check,rooms):
    if check not in rooms:
        rooms[check]=check+1
        return check
    empty=find(rooms[check],rooms)
    rooms[empty]=empty+1
    return empty

def solution(k, room_number):
    answer = []
    rooms={}
    for i in room_number:
        checkIn=find(i,rooms)
        answer.append(checkIn)
    return answer