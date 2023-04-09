n, m = map(int, input().split())
p = []

for i in range(m):
    p.append(int(input()))

p.sort()

price, max_revenue = 0, 0

for i in range(m):
    my_max = min(m-i, n)
    revenue = p[i] * my_max

    if revenue > max_revenue:
        max_revenue = revenue
        price = p[i]

print(price, max_revenue)