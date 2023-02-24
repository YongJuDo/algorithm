N, M = map(int, input().split())
basket = [(x + 1) for x in range(N)]

for _ in range(M):
    i, j = map(int, input().split())
    basket[i-1:j] = basket[i-1:j][::-1]

print(*basket, end = '')