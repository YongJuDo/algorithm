P, K = map(int, input().split())
cnt = 1

while True:
    if P == K:
        break
    else:
        cnt += 1
        K += 1
print(cnt)