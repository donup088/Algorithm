class Node:
    def __init__(self):
        self.removed=False
        self.prev=None
        self.next=None

def solution(n, k, cmd):
    node_arr=[Node() for _ in range(n)]
    for i in range(1,n):
        node_arr[i-1].next=node_arr[i]
        node_arr[i].prev=node_arr[i-1]
    
    cur=node_arr[k]
    deleted=[]
    for cm in cmd:
        if cm[0]=='U':
            x=int(cm[1:])
            for _ in range(x):
                cur=cur.prev
        elif cm[0]=='D':
            x=int(cm[1:])
            for _ in range(x):
                cur=cur.next
        elif cm[0]=='C':
            deleted.append(cur)
            cur.removed=True
            up=cur.prev
            down=cur.next
            if up!=None:
                up.next=down
            if down!=None:
                down.prev=up
                cur=down
            else:
                cur=up
        else:
            node=deleted.pop()
            node.removed=False
            up=node.prev
            down=node.next
            if up!=None:
                up.next=node
            if down!=None:
                down.prev=node
    answer = ''
    for i in range(n):
        if node_arr[i].removed:
            answer+='X'
        else:
            answer+='O'
    
    return answer