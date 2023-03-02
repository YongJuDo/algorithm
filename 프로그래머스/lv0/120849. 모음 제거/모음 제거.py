def solution(my_string):
    alpha = ['a', 'e', 'i', 'o', 'u']
    result = ''
    for i in my_string:
        if i not in alpha:
            result += i
    return result