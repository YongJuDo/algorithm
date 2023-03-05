def solution(num, k):
    num = str(num)
    result = 0
    for i in num:
        result += 1
        if i == str(k):
            return result
    return -1
    