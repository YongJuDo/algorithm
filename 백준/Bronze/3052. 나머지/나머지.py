arr = []
for _ in range(10):
    N = int(input())
    mod = N % 42
    arr.append(mod)

result = set(arr)
print(len(result))