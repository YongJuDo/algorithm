import sys

N = int(sys.stdin.readline())
tip_list = []
max_tip = 0

for _ in range(N):
    tip_list.append(int(sys.stdin.readline()))

tip_list.sort(reverse=True)

for i in range(N):
    total = tip_list[i] - i
    if total >= 0:
        max_tip += total
    else:
        break

print(max_tip)