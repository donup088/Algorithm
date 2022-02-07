def solution(m, musicinfos):
    answer = []
    m_list=[]
    for a in m:
        if not a.isalpha():
            m_list[-1]=m_list[-1]+a
        else:
            m_list.append(a)
    l=len(m_list)
    for i in range(len(musicinfos)):
        p_list=[]
        s,e,t,p=musicinfos[i].split(",")
        _s=s.split(":")
        _e=e.split(":")
        _time=(int(_e[0])-int(_s[0]))*60+int(_e[1])-int(_s[1])
        for a in p:
            if not a.isalpha():
                p_list[-1]=p_list[-1]+a
            else:
                p_list.append(a)
        pattern=[]
        
        for j in range(_time):
            pattern.append(p_list[j%len(p_list)])
        
        for j in range(len(pattern)):
            result=pattern[j:j+l]
            if result==m_list:
                answer.append((i,_time,t))
                break
    if len(answer)==0:
        return "(None)"
    answer = sorted(answer, key = lambda x: (-x[1], x[0]))
        
    return answer[0][2]