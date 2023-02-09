N = int(input())
total = 0

for i in range(1, N + 1):
    num = list(map(int, str(i)))
    total = sum(num) + i

    if total == N:
        print(i)
        break
    if i == N:
        print(0)