N = int(input())
cnt = N
for _ in range(N):
    alpha = input()
    for i in range(len(alpha)-1):
        if alpha[i] == alpha[i+1]:
            pass
        elif alpha[i] in alpha[i+1:]:
            cnt -= 1
            break

print(cnt)