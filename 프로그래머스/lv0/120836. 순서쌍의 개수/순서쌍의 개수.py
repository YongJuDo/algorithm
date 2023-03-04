def solution(n):
    result = []
    for i in range(1, n+1):
        if n % i == 0:
            result.extend([(i, n//i)])
    return len(result)