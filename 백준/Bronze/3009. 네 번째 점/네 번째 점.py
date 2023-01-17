x_dot = []
y_dot = []

for _ in range(3):
    x, y = map(int, input().split())
    x_dot.append(x)
    y_dot.append(y)

for i in range(3):
    if x_dot.count(x_dot[i]) == 1:
        x = x_dot[i]
    if y_dot.count(y_dot[i]) == 1:
        y = y_dot[i]

print(x, y)