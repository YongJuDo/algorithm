alpha = input().upper()
alpha_list = list(set(alpha))
cnt = []

for i in alpha_list:
    cnt.append(alpha.count(i))

if cnt.count(max(cnt)) > 1:
    print('?')
else:
    print(alpha_list[cnt.index(max(cnt))])