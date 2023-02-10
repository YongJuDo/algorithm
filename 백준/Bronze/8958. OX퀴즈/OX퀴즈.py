T = int(input())

for _ in range(T):
    quiz = list(input())
    cnt = 0
    result = 0
    for i in quiz:
        if i == 'O':
            cnt += 1
            result += cnt
        else:
            cnt = 0

    print(result)