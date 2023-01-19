n = int(input())
log_dic = {}

for _ in range(n):
    name, log = input().split()
    if log == 'enter':
        log_dic[name] = log
    else:
        del log_dic[name]

log_sort = sorted(log_dic.keys(), reverse=True)

for i in log_sort:
    print(i)