# x = int(input('2진수로 바꿀 숫자를 입력해주세요: '))
# result = ''
# while True:
#     if x % 2 == 0:
#         result += '0'
#     else:
#         result += '1'
#     x = x // 2
#     if x == 1:
#         result += str(x)
#         print(result[::-1])
#         break

# input은 들어온값이 스트링이니까 int로 바꿔줘야함.
# 마지막에[::-1] 이렇게 슬라이싱이 가능한 건 스트링이기때문에 result를 '' 이렇게 놧음.

def 이진수구하기(입력값):
    if 입력값 < 2:
        return str(입력값)
    else:
        return str(이진수구하기(입력값//2)) + str(입력값%2)

print(이진수구하기(11))
