def word(num):
    stack = []
    for i in range(num):
        k = str(input())
        stack.append(k)

    for i in range(1):
        for j in range(num-1):
            if stack[j][-1] != stack[j+1][0]:
                return "실패"
    return "통과"

print(word(3))