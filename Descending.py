# 숫자 n이 주어지고, n 개 만큼 무작위 수(0 <= x <= 100000)가 주어진다.
#  이를 내림차순으로 정렬하여 출력하여라.

# > 5
# > 22 31 42 50 12
# 50
# 42
# 31
# 22
# 12


n = int(input())
stack = []       

for i in range(n):          
        data = int(input())     
        stack.append(data)   

for j in range(0, len(stack)-1):   
    for k in range(0, len(stack)-1):
        if stack[k] > stack[k+1]:
            stack[k], stack[k+1] = stack[k+1], stack[k]
print()

for i in range(len(stack)):
    print(stack.pop())
