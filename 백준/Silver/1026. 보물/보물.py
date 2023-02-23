N = int(input())
A = sorted(list(map(int, input().split())))
B = list(map(int, input().split()))
S = 0

for i in A:
    j = B.pop(B.index(max(B)))
  
    S += i * j

print(S)