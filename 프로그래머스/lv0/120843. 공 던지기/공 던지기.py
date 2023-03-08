def solution(numbers, k):
    k = 2 * (k - 1) % len(numbers)
    return numbers[k]