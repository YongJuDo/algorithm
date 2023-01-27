stack = []

while True:
    duck = input()
    if duck == "고무오리 디버깅 끝":
        break
    if duck == "문제":
        stack.append("문제")
    elif duck == "고무오리":
        if stack:
            stack.pop()
        else:
            stack.append("문제")
            stack.append("문제")

if len(stack) == 0:
    print("고무오리야 사랑해")
else:
    print("힝구")