T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    N_arr = [list(map(int, input().split())) for _ in range(N)]
    M_arr = []

    for i in range(N - M + 1):
        for j in range(N - M + 1):
            cnt = 0
            for k in range(M):
                for l in range(M):
                    cnt += N_arr[i + k][j + l]
            M_arr.append(cnt)
            
    print(f'#{tc}', max(M_arr))
