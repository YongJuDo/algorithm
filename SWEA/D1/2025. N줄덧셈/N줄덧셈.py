#import sys
#sys.stdin = open("input_2025.txt", "r")
N = int(input())
sum = 0

for i in range(N + 1):
    sum += i
print(sum)