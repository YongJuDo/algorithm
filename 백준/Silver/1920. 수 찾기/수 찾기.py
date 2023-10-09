# 1920번 수 찾기 (이분탐색)
n = int(input())
n_list = list(map(int, input().split()))
m = int(input())
m_list = list(map(int, input().split()))
n_list.sort()

def binary_search(num):
    start = 0
    end = n - 1
    while start <= end:
        mid = (start + end) // 2
        if n_list[mid] == num:
            return True
        elif n_list[mid] < num:
            start = mid + 1
        else:
            end = mid - 1

for i in m_list:
    if binary_search(i):
        print(1)
    else:
        print(0)