T = int(input())

for _ in range(T):
    word = list(input())
    print(*word[0], *word[-1], sep = '')