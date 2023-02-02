W_score = []
K_score = []
for _ in range(10):
    W_score.append(int(input()))
for _ in range(10):
    K_score.append(int(input()))

W_score.sort()
K_score.sort()

print(sum(W_score[7:]), sum(K_score[7:]))