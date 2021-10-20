n = int(input())
body = []

for i in range(n):
    person = input()
    body.append(person.split(' '))

print(body)

for i in body:
    rank = n
    # print("1번 사람 몸무게:", i[0])
    for j in body:
        # print("2번 사람 몸무게:", j[0])
        if i[0] == j[0] or i[1] == j[1]:
            continue
        elif i[0] > j[0] or i[1] > j[1]:
            rank -= 1
    print(rank, end=' ')

# 5
# 55 185
# 58 183
# 88 186
# 60 175
# 46 155
