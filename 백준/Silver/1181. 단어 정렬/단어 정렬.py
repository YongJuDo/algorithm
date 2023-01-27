N = int(input())
alpha_list = []

for _ in range(N):
    alpha = input()
    alpha_list.append(alpha)

result_list = list(set(alpha_list))
result_list.sort()
result_list.sort(key = len)
print(*result_list, sep = '\n')