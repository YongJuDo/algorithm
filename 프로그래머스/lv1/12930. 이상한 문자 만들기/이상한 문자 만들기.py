def solution(s):
    s_list = s.split(' ')
    answer = []
    for i in s_list:
        word = ''
        for j in range(len(i)):
            if j % 2 == 0:
                word += i[j].upper()
            else:
                word += i[j].lower()
        answer.append(word)
    return ' '.join(answer)