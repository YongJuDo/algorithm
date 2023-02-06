people = []
sum = 0
for i in range(4):
    start, end = map(int, input().split())
    sum += end - start
    people.append(sum)

print(max(people))