T = int(input())

for tc in range(1, T + 1):
    N, K = map(int, input().split())
    grade = ['A+', 'A0', 'A-', 'B+', 'B0', 'B-', 'C+', 'C0', 'C-', 'D0']
    total_score = 0
    score_list = []

    for _ in range(N):
        mid, final, howk = map(int, input().split())
        total_score = (mid * 0.35) + (final * 0.45) + (howk * 0.2)
        score_list.append(total_score)

    k_index = score_list[K - 1]
    score_list.sort(reverse = True)
    k_score = score_list.index(k_index) // (N // 10)

    print(f'#{tc} {grade[k_score]}')