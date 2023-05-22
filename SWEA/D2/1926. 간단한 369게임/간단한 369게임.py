N = int(input())

for i in range(1, N + 1):
    s = str(i)
    clap = s.count('3') + s.count('6') + s.count('9')
    if clap != 0:
        print(clap * '-', end=' ')
    else:
        print(i, end = ' ')