def solution(emergency):
    result = []
    tmp = sorted(emergency, reverse=True)
    
    for i in emergency:
        result.append(tmp.index(i)+1)
            
            
    return result