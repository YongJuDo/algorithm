M = int(input())
ball = [0, 1, 0, 0]

for _ in range(M):
    X, Y = map(int, input().split())
    ball[X], ball[Y] = ball[Y], ball[X]

print(ball.index(1))