def solution(order):
    game = ['3', '6', '9']
    result = 0
    for i in str(order):
        if i in game:
            result += 1
        
    return result