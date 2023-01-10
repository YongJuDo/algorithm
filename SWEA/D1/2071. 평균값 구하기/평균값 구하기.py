tc = int(input())

for t in range(1, tc + 1):
    num = list(map(int, input().split()))
    avg = sum(num) / len(num)
   
    print(f"#{t} {round(avg)}") # round함수 -> 반올림