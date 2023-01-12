T = int(input())
date_dic = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
result = ''

for tc in range(1, T + 1):
    date = input()
    year = date[:4]
    month = date[4:6]
    day = date[6:]

    if (0 < int(month) < 13) and (int(day) <= date_dic[int(month)]):
        result = year + '/' + month + '/' + day
    else:
        result = -1

    print(f'#{tc} {result}')