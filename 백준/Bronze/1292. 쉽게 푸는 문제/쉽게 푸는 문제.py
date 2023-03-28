a, b = map(int, input().split())
num = []

for i in range(1, b+1):
    for j in range(i):
        num.append(i)

print(sum(num[a-1:b]))