T = 10
for _ in range(1, T  + 1):
    tc = int(input())
    num = list(map(int, input().split()))
    i = 1
    while True:
        if i > 5:
            i = 1
        temp = num.pop(0) - i
        if temp <= 0:
            num.append(0)
            break
        num.append(temp)
        i += 1
        
    print(f'#{tc}', *num)