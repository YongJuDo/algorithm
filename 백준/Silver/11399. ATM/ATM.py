N = int(input())
P = list(map(int, input().split()))
total = 0
P.sort()

for i in range(1, N + 1):
    total += sum(P[:i])

print(total)