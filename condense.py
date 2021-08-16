sentence = str(input()) + " "
char = sentence[0]
count = 1

for i in sentence[1:]:
    if char == i:
        count += 1
    else:
        print(char, end="")
        if count > 1:
            print(count, end= "")
        char = i
        count = 1
