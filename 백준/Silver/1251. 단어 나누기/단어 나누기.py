word = input()
word_list = []

for i in range(1, len(word) - 2):
    for j in range(i + 1, len(word)):
        one = word[:i]
        two = word[i:j]
        three = word[j:]

        word_total = one[::-1] + two[::-1] + three[::-1]
        word_list.append(word_total)

print(sorted(word_list)[0])