def solution(price, money, count):
    result = 0
    total_price = 0
    for i in range(1, count+1):
        total_price += price * i
        
    if money <= total_price:
        result = total_price - money
        return result
    else:
        return result