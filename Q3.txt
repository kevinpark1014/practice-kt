# Q3 Answer template

def solution(left, right):
    answer = 0
    i = 0
    for e in range(left,right+1):
        if e**(1/2) == int(e**(1/2)):
            answer -= e
        else:
            answer += e
        
    return answer

left = 13
right = 17
c = solution(left, right)
print(c)