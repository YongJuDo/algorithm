n = int(input())
num = 0

for i in range(1, n+1):
    num_han = list(map(int, str(i)))
    if i < 100:
        num += 1
    elif num_han[0] - num_han[1] == num_han[1] - num_han[2]:
        num +=1

print(num)
