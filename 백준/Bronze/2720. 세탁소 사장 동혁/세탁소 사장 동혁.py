T = int(input())
money_list = [25, 10, 5, 1]

for _ in range(T):
    money = int(input())
    C = []
    for i in money_list:
        C.append(money // i)
        money = money % i

    print(*C)