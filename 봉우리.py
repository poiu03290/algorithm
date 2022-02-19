# 봉우리
# 지도 정보가 N*N 격자판에 주어집니다. 각 격자에는 그 지역의 높이가 쓰여있습니다. 
# 격자판의 숫자 중 자신의 상하좌우 숫자보다 큰 숫자는 봉우리 지역입니다. 
# 봉우리 지역이 몇 개 있는 지 알아내는 프로그램을 작성하세요. 
# 격자의 가장자리는 0으로 초기화 되었다고 가정한다.
# 만약 N=5 이고, 격자판의 숫자가 다음과 같다면 봉우리의 개수는 10개입니다.

# 0 0 0 0 0 0 0
# 0 5 3 7 2 3 0
# 0 3 7 1 6 1 0
# 0 7 2 5 3 4 0
# 0 4 3 6 4 1 0
# 0 8 7 3 5 2 0
# 0 0 0 0 0 0 0

# ▣ 입력설명
# 첫 줄에 자연수 N이 주어진다.(1<=N<=50) 
# 두 번째 줄부터 N줄에 걸쳐 각 줄에 N개의 자연수가 주어진다. 각 자연수는 100을 넘지 않는다. 

# ▣ 출력설명
# 봉우리의 개수를 출력하세요.

# ▣ 입력예제 1 
# 5
# 5 3 7 2 3
# 3 7 1 6 1
# 7 2 5 3 4
# 4 3 6 4 1
# 8 7 3 5 2

# ▣ 출력예제 1
# 10




# n = int(input())
# a = [list(map(int, input().split())) for _ in range(n)]
# cnt = 0
# for i in range(n):
#     a[i].insert(0, 0)
#     a[i].append(0)
# a.insert(0, [0] * (n+2))
# a.append([0] * (n+2))

# for i in range(1, n+1):
#     for j in range(1, n+1):
#         if a[i][j] > a[i-1][j] and a[i][j] > a[i+1][j] and a[i][j] > a[i][j-1] and a[i][j] > a[i][j+1]:
#             cnt += 1
# print(cnt)

# 답변
import sys
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]
a.insert(0, [0] * n)
a.append([0] * n)
for x in a:
    x.insert(0, 0)
    x.append(0)
cnt = 0
for i in range(1, n+1):
    for j in range(1, n+1):
        if all(a[i][j] > a[i+dx[k]][j+dy[k]] for k in range(4)):   # all 함수는 모두가 참일때 참임.
            cnt += 1
print(cnt)