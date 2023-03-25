n = int(input())
num = []
i = 2

while i <= n:
    if n % i == 0:
        num.append(i)
        n = n // i
    else:
        i += 1
    
num.sort()

for i in num:
    print(i)
