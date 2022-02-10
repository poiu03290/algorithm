# 숫자만 추출
# 문자와 숫자가 섞여있는 문자열이 주어지면 그 중 숫자만 추출하여 그 순서대로 자연수를 만듭니다. 
# 만들어진 자연수와 그 자연수의 약수 개수를 출력합니다.
# 만약 “t0e0a1c2h0er”에서 숫자만 추출하면 0, 0, 1, 2, 0이고 이것을 자연수를 만들면 120이 됩니다. 
# 즉 첫 자리 0은 자연수화 할 때 무시합니다. 출력은 120를 출력하고, 다음 줄에 120의 약수의 개수를 출력하면 됩니다.
# 추출하여 만들어지는 자연수는 100,000,000을 넘지 않습니다.

# ▣ 입력설명
# 첫 줄에 숫자가 썩인 문자열이 주어집니다. 문자열의 길이는 50을 넘지 않습니다.

# ▣ 출력설명
# 첫 줄에 자연수를 출력하고, 두 번째 줄에 약수의 개수를 출력합니다.

# ▣ 입력예제 1 
# g0en2Ts8eSoft

# ▣ 출력예제 1
# 28
# 6

# import sys
# n = input()
# string = ''
# cnt = 0

# for i in str(n):
#     if i == '0' or i == '1' or i == '2' or i == '3' or i == '4' or i == '5' or i == '6' or i == '7' or i == '8' or i == '9':
#         string += i
# string = int(string)

# for i in range(1, string+1):
#     if string % i == 0:
#         cnt += 1
# print(string)
# print(cnt)


# 답변
import sys
s = input()
for x in s:
    # if x.isdigit    # 0 ~ 9까지의 숫자 뿐만아니라 알파벳이 아닌 숫자형태를 다 찾아줌(예: 2^2)
    if x.isdecimal():   # 0 ~ 9까지의 숫자를 찾아줌
        res = res * 10 + int(x)
print(res)
cnt = 0
for i in range(1, res+1):
    if res % i == 0:
        cnt += 1
print(cnt)
    


