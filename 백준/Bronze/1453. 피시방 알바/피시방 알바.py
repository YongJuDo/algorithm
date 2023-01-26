N = int(input())
customer = list(map(int, input().split()))
number = []
cnt = 0

for i in range(N):
    if customer[i] in number:
        cnt += 1
    else:
        number.append(customer[i])
print(cnt)