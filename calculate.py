import re
input = str(input())
splitInput = re.split(r'\+|-', input)
operatorIndex = []
result = 0

if input[0] != '-':
    input = '+' + input[0:]
elif input[0] == '-':
    del splitInput[0]

for i in range(len(input)):
    if input[i] == '+' or input[i] == '-':
        operatorIndex.append(i)

for i in range(len(splitInput)):
    try:
        result += int(input[operatorIndex[i]:operatorIndex[i+1]])
    except IndexError:
        result += int(input[operatorIndex[i]:])
print(result)