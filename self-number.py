list = []

for i in range(1, 10001):
    for j in str(i):
        i += int(j)
    list.append(i)


for i in range(1, 10001):
    if i not in list:
        print(i)