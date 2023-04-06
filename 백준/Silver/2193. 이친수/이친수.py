n = int(input())
arr = [[0 for j in range(2)] for i in range(n+1)]

arr[1][1] = 1
arr[1][0] = 0

for i in range(2, n+1):
    arr[i][0] = arr[i-1][0] + arr[i-1][1]
    arr[i][1] = arr[i-1][0]

print(arr[n][0] + arr[n][1])