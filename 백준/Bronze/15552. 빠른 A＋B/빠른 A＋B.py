import sys

past = int(sys.stdin.readline())

for i in range(past):
    a, b = map(int, sys.stdin.readline().split())
    print(a + b)