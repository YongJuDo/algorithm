N = int(input())

while True:
    check = True
    for s in str(N):
        if s != '4' and s != '7':
            check = False
            N -= 1
    if check:
        print(N)
        break