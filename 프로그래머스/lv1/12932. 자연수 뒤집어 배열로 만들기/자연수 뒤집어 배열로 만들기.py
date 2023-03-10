def solution(n):
    answer = []
    n = str(n)
    for i in n[::-1]:
        answer.append(int(i))
    return answer