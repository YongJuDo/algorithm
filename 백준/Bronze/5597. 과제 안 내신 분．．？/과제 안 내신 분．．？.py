num_list = [i for i in range(1, 31)]
for i in range(28):
    num = int(input())
    num_list.remove(num)

print(min(num_list))
print(max(num_list))
