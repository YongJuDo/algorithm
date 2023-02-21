A, B = map(str, input().split())
sum_min = int(A.replace('5', '6')) + int(B.replace('5', '6'))
sum_max = int(A.replace('6', '5')) + int(B.replace('6', '5'))
print(sum_max, sum_min)
