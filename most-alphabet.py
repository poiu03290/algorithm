input = list(input())
list = []

for i in input:
    list.append(input.count(i))

for i in range(1, len(input)):
    for j in range(len(input)-i):
        if list[j] < list[j+1]:
            continue  
        elif list[j] > list[j+1]:
            list[j], list[j+1] = list[j+1], list[j]
            input[j], input[j+1] = input[j+1], input[j]

print(input)
print(list)

if list[-1] == list[-list[-1]-1]:
    print('?')
elif list[-1] > list[-list[-1]-1]:
    print(input[-1])