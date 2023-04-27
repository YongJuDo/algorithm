T = int(input())

for tc in range(1, T+1):
    num = int(input())
    num_list = [2, 3, 5, 7, 11]
    array = [0] * 5
    
    for i in range(len(num_list)):
        while(num % num_list[i] == 0):
            array[i] += 1
            num //= num_list[i]

    print('#{} '.format(tc), end = '')
    print(*array)