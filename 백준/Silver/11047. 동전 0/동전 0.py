N, K = map(int, input().split())
coin_list = []
for _ in range(N):
    coin_list.append(int(input()))

cnt = 0
for i in coin_list[::-1]:
    cnt += K // i
    K %= i

print(cnt)