n = int(input())
vote = int(input())
stu = list(map(int, input().split()))
picture = [] 
score = [] 

for i in range(vote):
    if stu[i] in picture:
        for j in range(len(picture)): 
            if stu[i] == picture[j]:
                score[j] += 1 
    else:
        if len(picture) >= n: 
            for j in range(n):
                if score[j] == min(score): 
                    del picture[j]
                    del score[j]
                    break 
        picture.append(stu[i]) 
        score.append(1)

picture.sort()
for x in picture:
  print(x,end=' ')