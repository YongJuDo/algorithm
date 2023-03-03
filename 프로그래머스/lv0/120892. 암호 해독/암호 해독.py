def solution(cipher, code):
    result = ''
    for i in range(code-1, len(cipher), code):
        result += cipher[i]
    return result