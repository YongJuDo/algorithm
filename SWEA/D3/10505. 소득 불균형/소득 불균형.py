T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    num = list(map(int, input().split()))
    avg = sum(num) / N
    cnt = 0
    for i in num:
        if i <= avg:
            cnt += 1

    print(f'#{tc} {cnt}')