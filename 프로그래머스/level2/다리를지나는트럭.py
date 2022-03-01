from collections import deque

def solution(bridge_length, weight, truck_weights):
    answer = 1
    bridge_q=deque()
    t_l=truck_weights.pop(0)
    bridge_q.append([t_l,0])
    bridge_w=t_l
    while bridge_q:
        for i in range(len(bridge_q)):
            bridge_q[i][1]+=1
        if bridge_q[0][1]==bridge_length:
            a,b=bridge_q.popleft()
            bridge_w-=a
        if len(truck_weights)>0:
            tw=truck_weights[0]
            if len(bridge_q)<bridge_length and bridge_w+tw<=weight:
                tp=truck_weights.pop(0)
                bridge_q.append([tp,0])
                bridge_w+=tp
        answer+=1
    return answer