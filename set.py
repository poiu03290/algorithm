# 자료 구조 중에는 SET 이라는 자료구조가 있다. 
# 해당 SET은 중복된 후보군을 제거해주는 데, Python의 Set 자료구조를 직접 구현해보자.

# ['a', 'p', 'p', 'l', 'e'] => ['a', 'p', 'l', 'e']
# ['1', '12', '34', '56', '56', '1'] => ['1', '12', '34', '56']

def set(input):
    stack_1 = []
    stack_2 = []
    for i in input:
        stack_1.append(i) 

    for j in stack_1:
        if j not in stack_2:
            stack_2.append(j)
        
    return stack_2


print(set(['a', 'p', 'p', 'l', 'e']))
print(set(['1', '12', '34', '56', '56', '1']))
