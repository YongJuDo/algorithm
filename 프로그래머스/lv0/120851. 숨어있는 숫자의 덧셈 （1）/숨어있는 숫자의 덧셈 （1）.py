import re

def solution(my_string):
    result = re.findall('[1-9]', my_string)
    result = [int(i) for i in result]
    return sum(result)