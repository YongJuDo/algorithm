import re

def solution(my_string):
    find_string = re.findall('[0-9]+', my_string)
    result = 0
    for i in find_string:
        result += int(i)
    return result