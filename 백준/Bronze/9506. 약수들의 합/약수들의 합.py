while True:
    n = int(input())
    if n == -1:
        break
    num = []
    for i in range(1, n):
        if n % i == 0:
            num.append(i)
    if n == sum(num):
        print(f"{n} = {' + '.join(map(str, num))}")
    else:
        print(f'{n} is NOT perfect.')