T = int(input())
alpha_list = ['a', 'e', 'i', 'o', 'u']

for tc in range(1, T + 1):
    alpha = list(input())
    result = ''
    
    for i in alpha:
        if i not in alpha_list:
            result += i
    
    print(f'#{tc} {result}')