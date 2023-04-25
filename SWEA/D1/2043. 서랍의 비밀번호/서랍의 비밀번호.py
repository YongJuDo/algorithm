P, K = map(int, input().split())

count = 1
for i in range(P):
    if P != K:
        K += 1
        count += 1

print(count)