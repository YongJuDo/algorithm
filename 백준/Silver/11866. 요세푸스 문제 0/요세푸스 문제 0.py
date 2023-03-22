n, k = map(int, input().split())
queue = []
result = []

for i in range(1, n+1):
    queue.append(i)

idx = 0

while len(queue) > 0:
    idx = (idx + k - 1) % len(queue)
    result.append(str(queue.pop(idx)))


print(f"<{', '.join(result)}>")