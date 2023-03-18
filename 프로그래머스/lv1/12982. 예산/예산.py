def solution(d, budget):
    result = 0
    d.sort()
    for i in range(len(d)):
        if d[i] <= budget:
            budget -= d[i]
            result += 1
        
    return result