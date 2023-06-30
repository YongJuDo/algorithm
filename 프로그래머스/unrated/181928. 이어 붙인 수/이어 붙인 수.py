def solution(num_list):
    odd = 0
    even = 0
    for i in num_list:
        if i % 2 == 0:
            even = even * 10 + i
        else:
            odd = odd * 10 + i
    
    return even + odd