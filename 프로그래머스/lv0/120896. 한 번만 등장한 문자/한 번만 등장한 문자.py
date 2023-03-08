def solution(s):
    result = ''
    for i in s:
        if s.count(i) == 1:
            result += i

    return ''.join(sorted(result))