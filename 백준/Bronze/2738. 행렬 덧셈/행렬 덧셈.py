N, M = map(int, input().split())
arr_A = [list(map(int, input().split())) for _ in range(N)]
arr_B = [list(map(int, input().split())) for _ in range(N)]

for k in range(N):
    for l in range(M):
        print(arr_A[k][l] + arr_B[k][l], end = ' ')
    print()