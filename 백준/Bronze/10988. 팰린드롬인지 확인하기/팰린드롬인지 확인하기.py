word = list(input())
check_word = word[::-1]

if word == check_word:
    print(1)
else:
    print(0)