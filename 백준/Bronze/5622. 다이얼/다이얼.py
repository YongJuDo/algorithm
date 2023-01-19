dial_list = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
number = input()
time = 0

for i in range(len(number)):
    for j in dial_list:
        if number[i] in j:
            time += dial_list.index(j) + 3
print(time)