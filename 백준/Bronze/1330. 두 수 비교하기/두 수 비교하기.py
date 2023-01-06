values = input()
values = values.split()
a = int(values[0])
b = int(values[1])

if a > b:
    print('>')
elif a < b:
    print('<')
else:
    print('==')