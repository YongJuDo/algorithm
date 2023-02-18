C = int(input())

for _ in range(C):
    N = list(map(int, input().split()))
    avg = sum(N[1:]) / N[0]
    cnt = 0
    for i in N[1:]:
        if i > avg:
            cnt += 1

    rate = cnt / N[0] * 100
    print(f'{rate:.3f}%')