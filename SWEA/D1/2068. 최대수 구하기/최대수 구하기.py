tc = int(input())

for t in range(1, tc + 1):
    num = list(map(int, input().split()))
    max_num = max(num) # max함수 -> 가장 큰 값을 반환
    print(f"#{t} {max_num}")
