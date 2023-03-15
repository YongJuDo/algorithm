sum = 0
max_people = 0

for _ in range(10):
    out_people, in_people = map(int, input().split())
    sum = sum + (in_people - out_people)

    if sum > max_people:
        max_people = sum
    
print(max_people)