def solution(age):
    age_list = ["a","b","c","d","e","f","g","h","i","j"]
    result = ''
    for i in str(age):
        result += age_list[int(i)]
    return result