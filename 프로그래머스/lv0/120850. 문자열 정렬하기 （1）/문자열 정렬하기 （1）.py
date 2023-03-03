def solution(my_string):
    result = []
    for i in my_string:
        try:
            result.append(int(i))
        except:
            continue
    result.sort()
    return result