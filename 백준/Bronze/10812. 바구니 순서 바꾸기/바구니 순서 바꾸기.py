N, M = map(int, input().split())
basket = [x for x in range(1, N + 1)]

for _ in range(M):
    i, j, k = map(int, input().split())
    i, j, k = i-1, j-1, k-1
    basket[i:j + 1] = basket[k:j + 1] + basket[i:k]

print(*basket)