T = int(input())

for i in range(1, T + 1):
    P, Q, R, S, W = map(int, input().split())
    A_price = P * W
    B_price = Q

    if W > R:
        S_Price = S * (W - R)
        B_price = Q + S_Price

    if A_price > B_price:
        print('#' + str(i), B_price)
    else:
        print('#' + str(i), A_price)