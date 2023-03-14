N, K = map(int, input().split())
div = []

for i in range(1, N+1):
    if N % i == 0:
        div.append(i)

if K <= len(div):
    print(div[K-1])
else:
    print(0)