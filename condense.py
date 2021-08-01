sentence = str(input())
char = sentence[0]
cnt = 0

for i in range(len(sentence)):
    if char == sentence[i]:
        if i != len(sentence)-1:
            cnt += 1
        else: 
            cnt += 1
            print(char, end="")
            if cnt >= 2:
                print(cnt, end="")
    elif char != sentence[i]:
        if i != len(sentence)-1:
            print(char, end="")
            if cnt >= 2 :
                print(cnt, end="")
            char = sentence[i]
            cnt = 1
        elif i == len(sentence)-1:
            print(char, end="")
            if cnt >= 2:
                print(cnt, end="")
            char = sentence[i]
            cnt = 1
            print(char, end="")
            if cnt >= 2:
                print(cnt, end="")