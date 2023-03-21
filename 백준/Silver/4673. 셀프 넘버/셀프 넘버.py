numbers = set(range(1, 10001))
none_numers = set()

for num in numbers:
    for i in str(num):
        num += int(i)
    none_numers.add(num)

self_num = sorted(numbers - none_numers)
for j in self_num:
    print(j)