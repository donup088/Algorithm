def solution(gems):
    answer = []
    left = 0
    right = 0
    diff = 1e9
    gems_count = len(set(gems))
    d = {}
    while right < len(gems):
        if gems[right] not in d:
            d[gems[right]] = 1
        else:
            d[gems[right]] += 1
        right += 1
        if len(d) == gems_count:
            while left < right:
                if d[gems[left]] > 1:
                    d[gems[left]] -= 1
                    left += 1
                elif diff > right - left:
                    diff = right - left
                    answer = [left + 1, right]
                    break
                else:
                    break
    return answer
