N = list(input())
N.sort(reverse=True)
num = 0

if '0' not in N:
    print(-1)
else:
    for i in N:
        num += int(i)
    if num % 3 != 0:
        print(-1)
    else:
        print(''.join(N))