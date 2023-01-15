N = int(input())
v = list(map(int, input().split()))
con = int(input())

cnt = 0

for i in range(N):
    if v[i] == con:
        cnt += 1

print(cnt)