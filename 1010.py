T = int(input())
dy = [[0] * 30 for _ in range(30)]
for i in range(30):
    for j in range(30):
        if i == 1:
            dy[i][j] = j
        else:
            if i == j:
                dy[i][j] = 1
            elif i < j:
                dy[i][j] = dy[i-1][j-1] + dy[i][j-1]
for i in range(T):
    n, m = map(int, input().split())
    print(dy[n][m])