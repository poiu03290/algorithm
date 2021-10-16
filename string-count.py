input = str(input())
list = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
result = 0

for i in list:
    if 'c=' or 'c-' or 'dz=' or 'd-' or 'lj' or 'nj' or 's=' or 'z=' in input:
        input = input.replace(i, 'a')
    
for i in input:
    result += 1

print(result)