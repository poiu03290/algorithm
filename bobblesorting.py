n = int(input())
stack = []

for i in range(n):
    k = int(input())
    stack.append(k)

for i in range(n):
    for j in range(n-1):
        if stack[j] < stack[j+1]:
            continue
        elif stack[j] > stack[j+1]:
            stack[j], stack[j+1] = stack[j+1], stack[j]

print(stack)
for i in range(len(stack)):
    print(stack.pop())