# 1543번 - 문서 검색
word = input()
search = input()
cnt = 0
i = 0

while i <= len(word) - len(search):
    if word[i:i + len(search)] == search:
        cnt += 1
        i += len(search)
    else:
        i += 1

print(cnt)