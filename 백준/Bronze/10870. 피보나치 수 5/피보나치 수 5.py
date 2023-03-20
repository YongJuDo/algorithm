N = int(input())
sum = 0
Fibonacci = [0, 1]

for i in range(2, N+1):
    sum = Fibonacci[i-1] + Fibonacci[i-2]
    Fibonacci.append(sum)

print(Fibonacci[N])