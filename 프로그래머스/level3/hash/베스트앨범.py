def solution(genres, plays):
    play_count={}
    play={}
    answer = []
    for i in range(len(genres)):
        if play.get(genres[i])==None:
            tmp=[]
            tmp.append([plays[i],i])
            play[genres[i]]=tmp
            play_count[genres[i]]=plays[i]
        else:
            tmp=play[genres[i]]
            tmp.append([plays[i],i])
            play[genres[i]]=tmp
            play_count[genres[i]]+=plays[i]
            
    play_count=sorted(play_count.items(),key=lambda x:-x[1])
    
    for key,value in play_count:
        play[key]=sorted(play[key],key=lambda x:(-x[0],x[1]))
        res=play[key][:2]
        for r in res:
            answer.append(r[1])
    return answer