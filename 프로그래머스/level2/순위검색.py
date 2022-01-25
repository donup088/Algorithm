from itertools import combinations
from bisect import bisect_left


def solution(info, query):
    answer = []
    info_dict = {}

    for i in range(len(info)):
        info_split = info[i].split()  # info안의 문자열을 공백을 기준으로 분리
        keyword = info_split[:-1]  # info의 점수제외부분을 key로 분류
        score = info_split[-1]  # info의 점수부분을 value로 분류

        for j in range(5):  # key들로 만들 수 있는 모든 조합 생성
            for c in combinations(keyword, j):
                tmp = ''.join(c)
                print(tmp)
                if tmp in info_dict:
                    info_dict[tmp].append(int(score))  # 그 조합의 key값에 점수 추가
                else:
                    info_dict[tmp] = [int(score)]
    print(info_dict)

    for k in info_dict:
        info_dict[k].sort()  # dict안의 조합들을 점수순으로 정렬
    print(info_dict)
    for qu in query:  # query도 마찬가지로 key와 value로 분리
        myqu = qu.split(' ')
        qu_key = myqu[:-1]
        qu_val = myqu[-1]

        while 'and' in qu_key:  # and 제거
            qu_key.remove('and')
        while '-' in qu_key:  # - 제거
            qu_key.remove('-')
        qu_key = ''.join(qu_key)  # dict의 key처럼 문자열로 변경

        if qu_key in info_dict:  # query의 key가 info_dict의 key로 존재하면
            scores = info_dict[qu_key]

            if scores:  # score리스트에 값이 존재하면
                enter = bisect_left(scores, int(qu_val))

                answer.append(len(scores) - enter)
        else:
            answer.append(0)

    return answer


### 정확성 통과 효율성 실패
# def solution(info, query):
#     answer = []
#     info_list=[]
#     for i in range(len(info)):
#         tmp=info[i].split()
#         info_list.append(tmp)
    
#     for i in range(len(query)):
#         count=0
#         tmp=query[i].split(' and ')
#         a,b=tmp[-1].split()
#         tmp.pop()
#         tmp.append(a)
#         tmp.append(b)
        
        
#         for j in range(len(info_list)):
#             flag=0
    
#             if tmp[0]==info_list[j][0] or tmp[0]=='-':
#                 flag+=1
#             if tmp[1]==info_list[j][1] or tmp[1]=='-':
#                 flag+=1
#             if tmp[2]==info_list[j][2] or tmp[2]=='-':
#                 flag+=1
#             if tmp[3]==info_list[j][3] or tmp[3]=='-':
#                 flag+=1
#             if int(tmp[4])<=int(info_list[j][4]):
#                 flag+=1
#             if flag==5:
#                 count+=1
#         answer.append(count)
#     return answer