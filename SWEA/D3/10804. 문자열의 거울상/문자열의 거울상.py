T = int(input())

for tc in range(1, T + 1):
    str = list(input())
    str_dic = {'b': 'd', 'd':'b', 'p': 'q', 'q': 'p'}
    result = ''
    str.reverse()
    for i in str:
        result += str_dic[i]
        
    print(f'#{tc} {result}')