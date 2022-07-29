def solution(lottos, win_nums):
    answer = []
    cnt = 0
    min_ = 0
    for l in lottos:
        if l == 0:
            cnt += 1
            continue
        for w in win_nums:
            if l == w:
                min_ += 1
                break
                
    max_ = min_ + cnt
    if min_ < 2:
        return -1
    answer = [7-max_, 7-min_]
    return answer

lottos = [44, 1, 0, 0, 31, 25]
win_nums = [31, 10, 45, 1, 6, 19]
answer = solution(lottos, win_nums)
print(answer)