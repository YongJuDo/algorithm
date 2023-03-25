m = int(input())
n = int(input())

num = []
for i in range(m, n+1):
    cnt = 0
    if i > 1:
        for j in range(2, i):
            if i % j == 0:
                cnt += 1
                break
        if cnt == 0:
            num.append(i)

if len(num) == 0:
    print('-1')
else:
    print(sum(num))
    print(min(num))