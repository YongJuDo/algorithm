def solution(slice, n):
    if n % slice == 0:
        result = n / slice
    else:
        result = n // slice + 1
    return result
