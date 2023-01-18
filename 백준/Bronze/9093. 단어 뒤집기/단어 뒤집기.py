T = int(input())

for _ in range(T):
    word = list(input().split())
    for i in word:
        print(i[::-1], end = ' ') 
    print()