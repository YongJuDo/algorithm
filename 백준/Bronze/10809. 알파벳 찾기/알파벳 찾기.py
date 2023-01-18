S = list(input())
alpha = 'abcdefghijklmnopqrstuvwxyz'

for i in alpha:
    if i in S:
        print(S.index(i), end = ' ')
    else:
        print(-1, end = ' ') 