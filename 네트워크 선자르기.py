# 동적계획법이란? 네트워크 선 자르기(Bottom-Up)
# 현수는 네트워크 선을 1m, 2m의 길이를 갖는 선으로 자르려고 합니다.
# 예를 들어 4m의 네트워크 선이 주어진다면

# 1) 1m+1m+1m+1m
# 2) 2m+1m+1m
# 3) 1m+2m+1m
# 4) 1m+1m+2m
# 5) 2m+2m 

# 의 5가지 방법을 생각할 수 있습니다. (2)와 (3)과 (4)의 경우 왼쪽을 기준으로 자르는 위치가 다르면 다른 경우로 생각한다.
# 그렇다면 네트워크 선의 길이가 Nm라면 몇 가지의 자르는 방법을 생각할 수 있나요? 

# ▣ 입력설명
# 첫째 줄은 네트워크 선의 총 길이인 자연수 N(3≤N≤45)이 주어집니다.

# ▣ 출력설명
# 첫 번째 줄에 부분증가수열의 최대 길이를 출력한다.

# ▣ 입력예제 1 
# 7

# ▣ 출력예제 1
# 21


# Bottom-Up방식
import sys
n = int(input())
dy = [0] * (n+1)
dy[1] = 1   # 길이가 1m인 선을 자를때 방법이 1가지
dy[2] = 2   # 길이가 2m인 선을 자를때 방법이 2가지

for i in range(3, n+1):   # 길이가 3m ~ nm까지의 길이를 찾기위해
    dy[i] = dy[i-1] + dy[i-2]   # 해당식을 이용.
    
    # 만약 3m의 선을 자르는 방법을 구한다면? 
    # 선을 자르는 방법중 마지막 토막인 1m짜리를 자를텐데, 그럼 마지막1m 말고 앞의 2m의 선은 우리가 dy[2]에서 구했고, 
    # 그리고 2m를 자를텐데, 그럼 앞의 1m의 선은 dy[1]에서 구했지. 
    # 그럼 d[3] = dy[1] + dy[2] 의 식이 성립.
    # 여기서 1m와 2m의 방식만을 구한 이유는 문제에서 정해줬기때문. 
print(dy[n])


# Top-Down 방식
import sys
def DFS(len):
    if dy[len] > 0:   # 기본적으로 dy리스트는 0으로 초기화 되어있으니까 값이 들어갔다면 cut해주는거임!
        return dy[len]
    if len == 1 or len == 2:
        return len
    else:
        dy[len] = DFS(len-1) + DFS(len-2)   # 만약 n이 7이면, DFS(6) + DFS(5)를 dy라는 리스트의 7인덱스에 그값을 넣음.
        return dy[len]

if __name__ =="__main__":
    n = int(input())
    dy = [0] * (n+1)
    print(DFS(n))