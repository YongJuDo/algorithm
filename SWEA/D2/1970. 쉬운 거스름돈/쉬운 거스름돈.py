T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    money = [50000, 10000, 5000, 1000, 500, 100, 50, 10]
    print("#{} ".format(tc))
    for i in money:
        print(N // i, end=' ')
        N %= i
    print()
