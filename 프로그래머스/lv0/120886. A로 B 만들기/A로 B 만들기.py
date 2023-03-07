def solution(before, after):
    cnt = 0
    result = 0
    for i in before:
        if before.count(i) == after.count(i):
            cnt += 1
    if cnt == len(before):
        result = 1
    else:
        result = 0
    return result
        
    