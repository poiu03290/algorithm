# 대표값
# N명의 학생의 수학점수가 주어집니다. N명의 학생들의 평균(소수 첫째자리 반올림)을 구하고, 
# N명의 학생 중 평균에 가장 가까운 학생은 몇 번째 학생인지 출력하는 프로그램을 작성하세요.
# 평균과 가장 가까운 점수가 여러 개일 경우 먼저 점수가 높은 학생의 번호를 답으로 하고, 
# 높은 점수를 가진 학생이 여러 명일 경우 그 중 학생번호가 빠른 학생의 번호를 답으로 합니다.

# ▣ 입력설명
# 첫줄에 자연수 N(5<=N<=100)이 주어지고, 두 번째 줄에는 각 학생의 수학점수인 N개의 자연수가 주어집니다. 
# 학생의 번호는 앞에서부터 1로 시작해서 N까지이다.

# ▣ 출력설명
# 첫줄에 평균과 평균에 가장 가까운 학생의 번호를 출력한다.
# 평균은 소수 첫째 자리에서 반올림합니다.

# ▣ 입력예제 1 
# 10
# 45 73 66 87 92 67 75 79 75 80

# ▣ 출력예제 1
# 74 7

# 예제설명)
# 평균이 74점으로 평균과 가장 가까운 점수는 73(2번), 75(7번), 75(9번)입니다. 여기서 점수가 높은 
# 75(7번), 75(9번)이 답이 될 수 있고, 75점이 두명이므로 학생번호가 빠른 7번이 답이 됩니다.

# import sys
# n = int(input())
# a = list(map(int, input().split()))
# score = 0
# arrMin = a[0]

# for i in a:
#     score += i
# score = score / n
# score = round(score)

# for i in a:
#     if abs(score - i) < arrMin:
#         arrMin = abs(score - i)
#     print(score, a)


# 답변
import sys
n = int(input())
a = list(map(int, input().split()))

# round로 평균구하기
ave = round(sum(a)/n)   # round는 round_half_even 방식을 취한다. 즉, round(66.5)을 하면 66이 됨.(even, 즉 짝수쪽으로 값이 감.)

# round가 아닌 방식으로 평균구하기
ave = sum(a)/n
ave = ave + 0.5   # 0.5를 더해줌으로써 반올림을 해줌 (ave가 66.4면 66.9가 됨. 반대로 ave가 66.6이면 67.1이 됨.)
ave = int(ave)   # int로 형변환을 해주면 소수점이 떨어져 나감.

min = float('inf')

for idx, x in enumerate(a):
    tmp = abs(x - ave)
    if tmp < min:
        min = tmp
        score = x
        res = idx + 1
    elif tmp == min:
        if x > score:
            score = x
            res = idx + 1

print(ave, res)



