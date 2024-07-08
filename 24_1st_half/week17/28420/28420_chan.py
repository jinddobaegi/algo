# 회전역 앞에는 땅이 매우 많다. 이 땅에 우리는 캠핑카가 달린 차를 세우려고 한다. 
# 이때 캠핑카를 차 옆에 정확히 아래 그림의 3개의 모양으로만 배치할 수 있고, 캠핑카와 차는 회전하거나 뒤집힐 수 업다.

# 차와 캠핑카는 너비는 a로 같지만 차의 길이b와 캠핑카의 길이c는 다를 수 있다. 이때 너비는 차량의 좌우로 측정된 가로 폭 치수를,
# 길이는 차체의 앞부분에서 뒷부분까지의 치수를 의미한다. 땅은 1*1의 단위 구역마다 흐림 정도가 후어진다.
# 차와 캠핑카가 차지하는 단위 구역의 흐림정도 합이 낮을 수록 맑다. 단, 차와 캠핑카가 차지하는 단위 구역이 땅을 벗어나서는 안된다.
# 어떻게하면 가장 맑은 곳에서 캠핑할 수 있도록 차를 세울까?

# 아래 예시를 참고하자. 차와 캠핑카의 너비는 1, 차의 길이는 2 캠핑카의 길이는 3일 때, 아래 땅에 가장 맑은 위체에 차와 캠핑카를 배치하고 싶다.
# 예제 입력1의 땅은 아래와 같다. 해당 땅에 3가지 방법로 차를 놓을 수 있다고 했을 때, 차의 배치도는 3가지 방법 그대로이어야하나, 차의 앞부분의 위치는 달라질 수 있다.
# 단, 차체가 땅을 벗어나는 일은 없다. 아래와 같이 배치했을때 가장 맑은 곳에서 캠핑할 수 이싿. 이때의 흐림정도는 12이다.

# 입력
# 첫째줄에 땅의 세로와 가로의 길이 N,M이 공백으로 구분되어 주어진다.(2<=N,M<=300)
# 둘째줄에는 차와 캠핑카의 너비a, 차의 길이b, 캠핑카의 길이 c가 공백으로 구분되어 주어진다. 차와 캠핑카의 너비는 a로 동일하다.
# (1 \le a,b,c \le min(\frac{N}{2}, \frac{M}{2}))
# 셋째 줄부터 N개의 줄에 걸쳐 각 단위 구역의 흐림정도, Ai,j가 공백으로 구분되어 주어진다.
# 입력으로 주어지는 모든 수는 상수이다.

# 출력
# 가장 맑은 곳에서 캠핑할 때의 흐림 정도를 구하여라

# 1.왼쪽이 차, 오른쪽이 캠핑카인 일자 모양
# 2.기역자 모장인데 머리부분이 차, 꼬리부분이 캠핑카
# 3.기역자 모양인데 머리부분이 캠핑카, 꼬리부분이 차
# 이렇게 세가지 경우

# 차와 캠핑카의 너비a, 차의 길이b, 캠핑카의 길이 c
import sys
sys.stdin = open("week17/28420/28420.txt")

def calculate_min_blurriness():
    min_blurriness = float('inf')
    
    # Case 1: 일자 모양 (차가 왼쪽, 캠핑카가 오른쪽)
    for i in range(N - a + 1):
        for j in range(M - (b + c) + 1):
            current_blurriness = 0
            # 차의 흐림도 계산
            for x in range(i, i + a): #너비만큼
                for y in range(j, j + b):
                    current_blurriness += blurriness[x][y]
            # 캠핑카의 흐림도 계산
            for x in range(i, i + a): #
                for y in range(j + b, j + b + c):
                    current_blurriness += blurriness[x][y]
            min_blurriness = min(min_blurriness, current_blurriness)
    
    # Case 2: 기역자 모양 (머리 부분이 차, 꼬리 부분이 캠핑카)
    for i in range(N - (a + c) + 1):
        for j in range(M - (a + b) + 1):
            current_blurriness = 0
            # 차의 흐림도 계산
            for x in range(i, i + a):
                for y in range(j, j + b):
                    current_blurriness += blurriness[x][y]
            # 캠핑카의 흐림도 계산
            for x in range(i + a, i + a + c):
                for y in range(j, j + a):
                    current_blurriness += blurriness[x][y]
            min_blurriness = min(min_blurriness, current_blurriness)
    
    # Case 3: 기역자 모양 (머리 부분이 캠핑카, 꼬리 부분이 차)
    for i in range(N - (a + b) + 1):
        for j in range(M - (a + c) + 1):
            current_blurriness = 0
            # 캠핑카의 흐림도 계산
            for x in range(i, i + a):
                for y in range(j, j + c):
                    current_blurriness += blurriness[x][y]
            # 차의 흐림도 계산
            for x in range(i + a, i + a + b):
                for y in range(j, j + a):
                    current_blurriness += blurriness[x][y]
            min_blurriness = min(min_blurriness, current_blurriness)
    
    return min_blurriness

# 입력 처리
N, M = map(int, input().split())
a, b, c = map(int, input().split())
blurriness = [list(map(int, input().split())) for _ in range(N)]

# 결과 출력
print(calculate_min_blurriness())
