borad = input()

borad = borad.replace('XXXX', 'AAAA')
borad = borad.replace('XX', 'BB')

if 'X' in borad:
    print(-1)
else:
    print(borad)