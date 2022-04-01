# 알리바바와 40인의 도둑(Bottom-Up)
# 알리바바는 40인의 도둑으로부터 금화를 훔쳐 도망치고 있습니다.
# 알리바바는 도망치는 길에 평소에 잘 가지 않던 계곡의 돌다리로 도망가고자 한다.
# 계곡의 돌다리는 N×N개의 돌들로 구성되어 있다. 각 돌다리들은 높이가 서로 다릅니다.
# 해당 돌다리를 건널때 돌의 높이 만큼 에너지가 소비됩니다. 이동은 최단거리 이동을 합니다.
# 즉 현재 지점에서 오른쪽 또는 아래쪽으로만 이동해야 합니다. 
# N*N의 계곡의 돌다리 격자정보가 주어지면 (1, 1)격자에서 (N, N)까지 가는데 드는 에너지의 최소량을 구하는 프로그램을 작성하세요.
# 만약 N=3이고, 계곡의 돌다리 격자 정보가 다음과 같다면 

# 3 3 5
# 2 3 4
# 6 5 2

# (1, 1)좌표에서 (3, 3)좌표까지 가는데 드는 최소 에너지는 3+2+3+4+2=14이다.

# ▣ 입력설명
# 첫 번째 줄에는 자연수 N(1<=N<=20)이 주어진다. 
# 두 번째 줄부터 계곡의 N*N 격자의 돌다리 높이(10보다 작은 자연수) 정보가 주어진다.

# ▣ 출력설명
# 첫 번째 줄에 (1, 1)출발지에서 (N, N)도착지로 가기 위한 최소 에너지를 출력한다.

# ▣ 입력예제 1 
# 5
# 3 7 2 1 9
# 5 8 3 9 2
# 5 3 1 2 3
# 5 4 3 2 1 
# 1 7 5 2 4

# ▣ 출력예제 1
# 25

import sys
if __name__ == "__main__":
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    dy = [[0] * n for _ in range(n)]
    dy[0][0] = arr[0][0]   # 다이나믹 테이블의 첫자리는 arr과 같음.
    
    for i in range(n):   # 애초에 첫번째행과 첫번째열은 그 전에서만 올수있으니 다음처럼 값을 넣어준다.
        dy[0][i] = dy[0][i-1] + arr[0][i]
        dy[i][0] = dy[i-1][0] + arr[i][0]
    
    for i in range(1, n):  # 2중 for문으로 값을 탐색.
        for j in range(1, n):  # (0, 0)은 정해놨으니 1부터 시작
            dy[i][j] = min(dy[i-1][j], dy[i][j-1]) + arr[i][j]
    
    print(dy[n-1][n-1]) # 인덱스번호때매 다음과 같이 출력.


# Top-Down 방식
import sys
def DFS(x, y):
    if dy[x][y] > 0:
        return dy[x][y]
    if x == 0 and y == 0:
        return arr[0][0]
    else:
        if x == 0:   # x가 0이라면 벽에 붙은 상황이니, x값은 그대로 y값은 1을 빼준다.
            dy[x][y] = DFS(x, y-1) + arr[x][y]   # 각 dy[x][y]에 메모리제이션을 해서 마지막에 한번에 return함
            return 
        elif y == 0:
            dy[x][y] = DFS(x-1, y) + arr[x][y]
        else:
            dy[x][y] = min(DFS(x-1, y), DFS(x, y-1)) + arr[x][y]   # x축이나 y축에서 작은값을 현재값과 더해준다.
        return dy[x][y]

if __name__ == "__main__":
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    dy = [[0] * n for _ in range(n)]
    print(DFS(n-1, n-1))