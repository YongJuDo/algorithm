n = int(input())
cow = []

for _ in range(n):
    cow.append(list(map(int, input().split())))

cow.sort()

min_time = 0

for start, delay in cow:
    if min_time < start:
        min_time = start + delay

    else:
        min_time += delay
print(min_time)