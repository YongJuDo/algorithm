T = int(input())

for tc in range(1, T + 1):
    a, b, c = map(int, input().split())
    d = 0
    if a == b:
        d = c
    else:
        if b == c:
            d = a
        else:
            d = b
            
    print(f'#{tc} {d}')