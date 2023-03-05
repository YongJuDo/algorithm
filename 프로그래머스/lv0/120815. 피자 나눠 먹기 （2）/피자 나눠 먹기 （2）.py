def solution(n):
    result = 1
    while (result * 6) % n != 0:
        result += 1
    return result