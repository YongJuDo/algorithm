def solution(array, n):
    result = 0
    array.sort()
    check = n + 100
    for i in array:
        if abs(i-n) < check:
            check = abs(i-n)
            result = i
    
    return result