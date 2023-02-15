mush = []
total = 0
for _ in range(10):
    score = int(input())
    mush.append(score)
for i in mush:
    total += i
    if total >= 100:
        if total - 100 > 100 - (total - i):
            total -= i
        break

print(total)