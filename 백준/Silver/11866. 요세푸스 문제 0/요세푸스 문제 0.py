from collections import deque
n, k = map(int, input().split())
queue = deque()
result = []

for i in range(1, n+1):
    queue.append(i)

while len(queue) > 0:
    for i in range(k-1):
        queue.append(queue.popleft())
    result.append(str(queue.popleft()))


print(f"<{', '.join(result)}>")
