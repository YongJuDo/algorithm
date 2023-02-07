import sys
input = sys.stdin.readline

N = int(input())
stack = []
cnt = 1

for _ in range(N):
    stack.append(int(input()))

last_value = stack[-1]

for i in reversed(range(N)):
    if stack[i] > last_value:
        cnt += 1
        last_value = stack[i]

print(cnt)