N = int(input())
Pi = list(map(int, input().split()))
result = 0
way = []

for i in range(1, N):
    if Pi[i] > Pi[i - 1]:
        result += Pi[i] - Pi[i - 1]
        if i == N - 1:
            way.append(result)
    else:
        way.append(result)
        result = 0

print(max(way))