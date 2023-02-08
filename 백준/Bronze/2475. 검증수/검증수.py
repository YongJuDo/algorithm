N = list(map(int, input().split()))
result = 0

for i in N:
    result += i ** 2

print(result % 10)