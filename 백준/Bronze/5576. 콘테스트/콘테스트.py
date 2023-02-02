W_score = []
K_score = []
for _ in range(10):
    W_score.append(int(input()))
for _ in range(10):
    K_score.append(int(input()))

W_score.sort(reverse=True)
K_score.sort(reverse=True)

print(sum(W_score[:3]), sum(K_score[:3]))