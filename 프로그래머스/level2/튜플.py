def solution(s):
    answer = []
    l=[]
    s=s[1:len(s)-1]
    s=list(s)
    for i in range(len(s)-1):
        if s[i]==',' and s[i+1]=='{':
            s[i]='|'
    if '|' in s:
        s.remove('|')
    tmp=''
    stack=[]
    for i in range(len(s)):
        if s[i].isdigit():
            tmp+=s[i]   
        elif s[i]==',':
            stack.append(tmp)
            tmp=''
        elif s[i]=='}':
            stack.append(tmp)
            l.append(stack)
            tmp=''
            stack=[]
    l.sort(key=len)
    
    temp=[]
    for i in range(len(l)):
        for j in range(len(l[i])):
            if l[i][j] not in temp:
                temp.append((l[i][j]))
    for t in temp:
        answer.append(int(t))
    return answer

# 다른사람의 풀이
# def solution(s):
#     # {{, }}를 제거 후 },{ 으로 나누기
#     data = s[2:-2].split("},{")
#     # 길이 별로 오름차순 정렬
#     data = sorted(data, key=lambda x: len(x))
#     answer = []
#     for item in data:
#         # 각각의 원소로 분류 후
#         item = list(map(int, item.split(",")))
#         for value in item:
#             # 포함되어 있지 않으면 input  
#             if value not in answer:
#                 answer.append(value)
#     return answer