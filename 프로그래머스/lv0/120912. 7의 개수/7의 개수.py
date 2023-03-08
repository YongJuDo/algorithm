def solution(array):
    result = ''
    for i in array:
        result += str(i)
        
    return result.count('7')