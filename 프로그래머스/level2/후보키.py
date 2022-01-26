from itertools import combinations

def solution(relation):
    col=len(relation[0])
    key_idx=list(range(col))
    candidates=[]
    for i in range(1,col+1):
        for comb in combinations(key_idx,i):
            tmp=[]
            for r in relation:
                c_key=[r[c] for c in comb]
                if c_key in tmp:
                    break
                else:
                    tmp.append(c_key)
            else:
                for c in candidates:
                    if set(c).issubset(set(comb)):
                        break
                else:
                    candidates.append(comb)            
    return len(candidates)