def solution(rsp):
    num = {'2': '0', '0': '5', '5': '2'}
    result = ''
    for i in rsp:
        result += num.get(i)
    return result