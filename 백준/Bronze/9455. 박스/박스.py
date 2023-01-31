T = int(input())
for _ in range(T):
    n, m = map(int, input().split())
    box = [input().split() for _ in range(n)]
    result = 0
    for i in range(m):
        cnt = 0
        for j in range(n-1, -1, -1):
            if box[j][i] == '1':
                result += cnt
            else:
                cnt += 1
    print(result)