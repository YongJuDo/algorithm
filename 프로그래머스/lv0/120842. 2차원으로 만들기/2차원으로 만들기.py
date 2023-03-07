def solution(num_list, n):
    result = []
    j = 0
    for i in range(n, len(num_list) + n, n):
        result.append(num_list[j:i])
        j += n
    return result