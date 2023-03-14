T = int(input())

for _ in range(T):
    n = bin(int(input()))[2:]
    
    for i, v in enumerate(n[::-1]):
        if v == '1':
            print(i, end = ' ')