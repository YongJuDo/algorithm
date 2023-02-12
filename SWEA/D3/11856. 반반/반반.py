T = int(input())

for tc in range(1, T + 1):
    S = list(input())
    check = True

    for i in S:
        if S.count(i) != 2:
            check = False
    
    if check == True:
        print(f'#{tc} Yes')
    else:
        print(f'#{tc} No')