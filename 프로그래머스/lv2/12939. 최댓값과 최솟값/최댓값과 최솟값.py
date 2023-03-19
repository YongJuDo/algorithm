def solution(s):
    s_list = list(map(int, s.split(' ')))
    s_list.sort()
    
    return str(min(s_list)) + " " + str(max(s_list))