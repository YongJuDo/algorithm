def solution(hp):
    a = hp // 5
    b = (hp - (5 * a)) // 3
    c = (hp - (5 * a) - (3 * b)) // 1
    return a + b + c