from itertools import permutations 

def ban_check(users,banned_id):
    for i in range(len(banned_id)):
        if len(users[i])!=len(banned_id[i]):
            return False
        for j in range(len(users[i])):
            if banned_id[i][j]=='*':
                continue
            if users[i][j]!=banned_id[i][j]:
                return False
    return True

def solution(user_id, banned_id):
    user_permutations=list(permutations(user_id,len(banned_id)))
    ban=[]
    for users in user_permutations:
        if not ban_check(users,banned_id):
            continue
        else:
            users=set(users)
            if users not in ban:
                ban.append(users)
    return len(ban)