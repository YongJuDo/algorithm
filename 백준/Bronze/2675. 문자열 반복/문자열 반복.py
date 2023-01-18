T = int(input())

for _ in range(T):
    R, S = input().split()
    text = ''
    for i in S:
        print(int(R) * i, end = '')
    print()