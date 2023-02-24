N, M = map(int, input().split())
ball = [(x + 1) for x in range(N)]

for _ in range(M):
    i, j = map(int, input().split())
    ball[i - 1], ball[j - 1] = ball[j - 1], ball[i - 1]

print(*ball, end = '')