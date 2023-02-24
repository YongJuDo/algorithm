N, M = map(int, input().split())
ball = [0] * N

for _ in range(M):
    i, j, k = map(int, input().split())
    for x in range(i, j + 1):
        ball[x - 1] = k

print(*ball, end = '')