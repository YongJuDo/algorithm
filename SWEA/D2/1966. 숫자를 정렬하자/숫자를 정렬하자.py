T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    num = list(map(int, input().split()))
    num.sort()
    print(f'#{tc} ', end = '')
    print(*(num))