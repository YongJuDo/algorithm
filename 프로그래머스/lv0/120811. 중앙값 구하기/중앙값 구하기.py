def solution(array):
    array.sort()
    mid_array = len(array) // 2
    return array[mid_array]