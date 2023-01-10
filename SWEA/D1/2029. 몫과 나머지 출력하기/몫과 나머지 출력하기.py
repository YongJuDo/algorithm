tc = int(input())

for t in range(1, tc + 1):
    a, b = list(map(int, input().split()))
    div = a // b # 몫 계산
    mod = a % b # 나머지 계산
    print(f"#{t} {div} {mod}")