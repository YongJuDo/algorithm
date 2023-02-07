N = int(input())
size_list = []

for _ in range(N):
    x, y = map(int, input().split())
    size_list.append((x, y))

for i in size_list:
    rank = 1
    for j in size_list:
        if i[0] < j[0] and i[1] < j[1]:
            rank += 1

    print(rank, end = ' ')