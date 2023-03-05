def solution(my_string):
    result = ''
    for i in my_string:
        result += i.lower()
    result = ''.join(sorted(result))
    return result