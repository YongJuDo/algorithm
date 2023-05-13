T = int(input())

for i in range(1, T + 1):
    palindrome = str(input())
    if palindrome[:len(palindrome)] == palindrome[::-1]:
        print('#' + str(i), 1)
    else:
        print('#' + str(i), 0)