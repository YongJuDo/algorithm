T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    num_list = [0] * 10
    cnt = 0
    while True:
        if 0 not in num_list:
            break
        else:
            cnt += 1
            num = str(N * cnt)
            for i in range(len(num)):
                num_list[int(num[i])] = 1

    print(f'#{tc} {num}')