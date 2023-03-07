N = int(input())
price = []
total = 0

for _ in range(N):
    price.append(int(input()))

price.sort(reverse=True)

for i in range(N):
    if i % 3 != 2:
        total += price[i]

print(total)