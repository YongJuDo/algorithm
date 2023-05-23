T = int(input())
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

for tc in range(1, T + 1):
    N = int(input())
    arr = [[0] * N for _ in range(N)]
    i, j, cnt, dr = 0, 0, 1, 0
    arr[i][j] = cnt
    cnt += 1

    while cnt <= N * N:
        nx, ny = i + dx[dr], j + dy[dr]
        if 0 <= nx < N and 0 <= ny < N and arr[nx][ny] == 0:
            i, j = nx, ny
            arr[i][j] = cnt
            cnt += 1
        else:
            dr = (dr + 1) % 4

    print(f'#{tc}')
    for lis in arr:
        print(*lis)