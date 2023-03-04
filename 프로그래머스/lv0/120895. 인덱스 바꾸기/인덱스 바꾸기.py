def solution(my_string, num1, num2):
    result = ''
    my_string = list(my_string)
    my_string[num1], my_string[num2] = my_string[num2], my_string[num1]
    return result.join(my_string)