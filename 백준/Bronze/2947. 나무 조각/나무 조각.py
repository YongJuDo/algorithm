tree = list(map(int, input().split()))

while True:
    for i in range(4):
        if tree[i] > tree[i + 1]:
            tree[i], tree[i + 1] = tree[i + 1], tree[i]
            print(*tree)

    if tree == [1, 2, 3, 4, 5]:
        break
