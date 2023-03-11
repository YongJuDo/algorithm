def solution(n):
    result = 0
    num = n ** 0.5
    if num == int(num):
        return (num + 1) ** 2
    else:
        return -1