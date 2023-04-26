T = int(input())

for i in range(1, T+1):
    date = str(input())
    days = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
    year = date[:4]
    month = date[4:6]
    day = date[6:]

    slash = ''
    if 0 < int(month) < 13 and int(day) <= days[int(month)]:
        slash = year + '/' + month + '/' + day
    else:
        slash = '-1'

    print('#' + str(i), slash)