def solution(sides):
    if sum(sides) - max(sides) <= max(sides):
        return 2
    else:
        return 1