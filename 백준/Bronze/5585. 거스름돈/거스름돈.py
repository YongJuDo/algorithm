pay = 1000 - int(input())
pay_list = [500, 100, 50, 10, 5, 1]
cnt = 0
for i in pay_list:
    cnt += pay // i
    pay %= i

print(cnt)