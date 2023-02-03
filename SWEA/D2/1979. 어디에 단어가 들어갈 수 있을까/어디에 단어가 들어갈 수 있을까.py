T = int(input())

for tc in range(1, T + 1):
    N, K = map(int, input().split())
    N_arr = [list(map(int, input().split())) for _ in range(N)]
    k_len = 0
    
    for i in range(N):
        cnt = 0
        for j in range(N):
            if N_arr[i][j] == 1:
                cnt += 1
            if N_arr[i][j] == 0 or j == N - 1:
                if cnt == K:
                    k_len += 1
                cnt = 0
    
    for i in range(N):
        cnt = 0
        for j in range(N):
            if N_arr[j][i] == 1:
                cnt += 1
            if N_arr[j][i] == 0 or j == N - 1:
                if cnt == K:
                    k_len += 1
                cnt = 0
    
    print(f'#{tc} {k_len}')