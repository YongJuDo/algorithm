tc = int(input())

for t in range(1, tc + 1):
    num = list(map(int, input().split()))
    sum = 0
    avg = 0

    for i in num:
        sum += i
        avg = sum / 10
    
    print(f"#{t} {round(avg)}")