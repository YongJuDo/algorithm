A, B = map(int, input().split())
A_elem = set(list(map(int, input().split())))
B_elem = set(list(map(int, input().split())))
print(len(A_elem - B_elem) + len(B_elem - A_elem))