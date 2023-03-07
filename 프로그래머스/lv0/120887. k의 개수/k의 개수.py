def solution(i, j, k):
    result = 0
    for x in range(i, j+1):
        for y in str(x):
            if y == str(k):
                result += 1
    return result