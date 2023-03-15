def solution(left, right):
    result = 0
    for i in range(left, right+1):
        div_cnt = 0
        for j in range(1, i+1):
            if i % j == 0:
                div_cnt += 1
                
        if div_cnt % 2 == 0:
            result += i
        else:
            result -= i
                
                
    return result