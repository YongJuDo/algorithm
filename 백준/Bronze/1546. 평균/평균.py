N = int(input())
number = list(map(int, input().split()))
m = max(number)

sum = 0
for i in number:
    i = i / m * 100
    sum += i

print(sum / N)