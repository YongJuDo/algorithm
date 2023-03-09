def solution(my_str, n):
    result = []
    for i in range(0, len(my_str), n):
        result.append(my_str[:n])
        my_str = my_str[n:]
            
    return result