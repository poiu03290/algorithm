# 격자판 최대합
# 5*5 격자판에 아래와 같이 숫자가 적혀있습니다. 

# 10 13 10 12 15
# 12 39 30 23 11
# 11 25 50 53 15
# 19 27 29 37 27
# 19 13 30 13 19

# N*N의 격자판이 주어지면 각 행의 합, 각 열의 합, 두 대각선의 합 중 가장 큰 합을 출력합니다.

# ▣ 입력설명
# 첫 줄에 자연수 N이 주어진다.(1<=N<=50) 
# 두 번째 줄부터 N줄에 걸쳐 각 줄에 N개의 자연수가 주어진다. 각 자연수는 100을 넘지 않는다. 

# ▣ 출력설명
# 최대합을 출력합니다.

# ▣ 입력예제 1 
# 5
# 10 13 10 12 15
# 12 39 30 23 11
# 11 25 50 53 15
# 19 27 29 37 27
# 19 13 30 13 19

# ▣ 출력예제 1
# 155

# import sys
# n = int(input())
# rowSum = 0
# columnSum = 0
# revDiagonalSum = 0
# diagonalSum = 0
# rowMax = -2147000000
# columnSumMax = -2147000000
# result = -2147000000
# stack = []
# for i in range(n):
#     a = list(map(int, input().split()))
#     if sum(a) > rowMax:
#         rowMax = sum(a)
#         rowSum = rowMax
#     diagonalSum += a[i]
#     revDiagonalSum += a[-1-i]
#     columnSum += a[i-i]
#     if columnSum > columnSumMax:
#         columnSumMax = columnSum
# stack.append(diagonalSum)
# stack.append(revDiagonalSum)
# stack.append(columnSumMax)
# stack.append(rowSum)

# for i in range(len(stack)):
#     if stack[i] > result:
#         result = stack[i]
# print(result)

# 답변
# import sys
n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]  # for 문으로 n번 돌려서 입력받은 수를 2차원 리스트로 만들기
largest = -2147000000
for i in range(n):
    sum1 = sum2 = 0
    for j in range(n):
        sum1 += a[i][j]
        sum2 += a[j][i]
    if sum1 > largest:
        largest = sum1
    if sum2 > largest:
        largest = sum2
sum1 = sum2 = 0
for i in range(n):
    sum1 += a[i][i]
    sum2 += a[i][n-i-1]
if sum1 > largest:
    largest = sum1
if sum2 > largest:
    largest = sum2
print(largest)
