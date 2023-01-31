N = int(input())
matrix = [list(input()) for _ in range(N)]
row, column = 0, 0 

for i in range(N):
    cnt = 0
    for j in range(N):
        if matrix[i][j] == '.':
            cnt += 1
        else:
            cnt = 0
        if cnt == 2:
            row += 1

for i in range(N):
    cnt = 0
    for j in range(N):
        if matrix[j][i] == '.':
            cnt += 1
        else:
            cnt = 0
        if cnt == 2:
            column += 1

print(row, column)