# Anagram(아나그램 : 구글 인터뷰 문제)
# Anagram이란 두 문자열이 알파벳의 나열 순서를 다르지만 그 구성이 일치하면 두 단어는 아나그램이라고 합니다. 
# 예를 들면 AbaAeCe 와 baeeACA 는 알파벳을 나열 순서는 다르지만 그 구성을 살펴보면 
# A(2), a(1), b(1), C(1), e(2)로 알파벳과 그 개수가 모두 일치합니다. 
# 즉 어느 한 단어를 재배열하면 상대편 단어가 될 수 있는 것을 아나그램이라 합니다.
# 길이가 같은 두 개의 단어가 주어지면 두 단어가 아나그램인지 판별하는 프로그램을 작성하세요. 
# 아나그램 판별시 대소문자가 구분됩니다.

# ▣ 입력설명
# 첫 줄에 첫 번째 단어가 입력되고, 두 번째 줄에 두 번째 단어가 입력됩니다. 
# 단어의 길이는 100을 넘지 않습니다. 

# ▣ 출력설명
# 두 단어가 아나그램이면 "YES"를 출력하고, 아니면 "NO"를 출력합니다.

# ▣ 입력예제 1 
# AbaAeCe
# baeeACA

# ▣ 출력예제 1
# YES

# for i in range(n):
#     word = input()
#     p[word] = 1

# import sys
a = input()
b = input()
str1 = dict()
str2 = dict()
for x in a:
    str1[x] = str1.get(x, 0) + 1
for x in b:
    str2[x] = str2.get(x, 0) + 1

for i in str1.keys():
    if i in str2.keys():
        if str1[i] != str2[i]:
            print("NO")
            break
    else:
        print("NO")
        break
else:
    print("YES")

# 개선된 코드
# a = input()
# b = input()
# sH = dict()
# for x in a:
#     sH[x] = sH.get(x, 0) + 1
# for x in b:
#     sH[x] = sH.get(x, 0) - 1
# for x in a:
#     if sH.get(x) > 0:
#         print("NO")
#         break
# else:
#     print("YES")

# 리스트 이용 (아스키number 이용)
import sys
a = input()
b = input()
str1 = [0] * 52
str2 = [0] * 52
for x in a:
    if x.isupper():
        str1[ord(x) - 65] += 1  # ord는 python문법으로 아스키숫자로 바꿔줌, 대문자A는 65, 대문자B는 66
    else:                       # 때문에 대문자즈 65를 뺴줘야 0번이 A, 1번이 B로 감
        str1[ord(x) - 71] += 1  # 소문자는 71을 빼줌
for x in b:
    if x.isupper():
        str2[ord(x) - 65] += 1
    else:
        str2[ord(x) - 71] += 1
# for i in range(52):
#     if str1[i] != str2[i]:
#         print("NO")
#         break
# else:
#     print("YES")
if str1 == str2:  # 파이썬은 이렇게도 가능.
    print("YES")
else:
    print("NO")