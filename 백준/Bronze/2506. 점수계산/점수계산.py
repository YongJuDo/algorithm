N = int(input())
num = list(map(int, input().split()))
score = 0
cnt = 0

for i in range(N):
    if num[i] == 1:
        cnt += 1
        score += cnt
    else:
        cnt = 0
print(score)