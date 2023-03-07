N = int(input())
km = list(map(int, input().split()))
L_Price = list(map(int, input().split()))
min_Price = L_Price[0]
cost = 0

for i in range(N-1):
    if min_Price > L_Price[i]:
        min_Price = L_Price[i]
    
    cost += min_Price * km[i]

print(cost)