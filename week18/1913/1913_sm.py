# 달팽이
# 실버3

# 문제
'''
홀수인 자연수 N이 주어지면, 다음과 같이 1부터 N2까지의 자연수를 달팽이 모양으로 N×N의 표에 채울 수 있다.
N이 주어졌을 때, 이러한 표를 출력하는 프로그램
N2 이하의 자연수가 하나 주어졌을 때, 그 좌표도 함께 출력
N=5인 경우 6의 좌표는 (4,3)

'''

# 풀이법
'''
2차원 배열을 나선형으로 채워나가면서  숫자 위치 찾아
그 과정에서 숫자의 위치를 기록하고, 마지막으로 해당 위치를 출력하고
배열의 모든 행을 출력하고, 1부터의 순서를 출력 ㄱ
'''
# 틀렸는데 어딜 고쳐야될지 모르곘어요
import sys
input = sys.stdin.readline

# 입력
n = int(input()) # 홀수인 자연수
location = int(input()) # 위치를 찾으려고 하는 n제곱 이하의 자연수
# 2차원 좌표 생성 (여기다가 숫자 채워넣을 거임)
graph = [[0 for _ in range(n)] for _ in range(n)]


# 4방향으로 이동할 거
dy =[0, 1, 0, -1]
dx =[1, 0, -1, 0]

# 시작 좌표 (0,0)
x, y = 0, 0

# 채워야 할 마지막 숫자(가장큰 n제곱의 인덱스가 n제곱 -1)
num = n*n - 1
# 중앙 위치에 n제곱 값 저장
graph[x][y] = n*n

# 탐색
while True:
    # 상하좌우 돌면서
    for i in range(4):
        # 이동할 수 있을 때까지 반복
        while True:
            # x, y 좌표
            x = x + dx[i]
            y = y + dy[i]

            # 범위를 벗어나거나 이미 값이 존재하는 경우
            if x >= n or y >= n or x < 0 or y < 0 or graph[x][y] != 0:
                # 이전 위치로
                x -= dx[i]
                y -= dy[i]
                break # 중단
            else:
                # 현재 위치 저장
                graph[x][y] = num

                # 찾고자 하는 숫자를 찾은 경우
                if graph[x][y] == location:
                    new_x, new_y = x, y
                # 다음 숫자로 이동
                num -= 1

                print(x, y) # 현재 위치
                print(graph) # 현재 배열

    # 중앙 위치에 오면
    if x == n//2 and y == n//2:
        break # 종료


# 배열 행 출력
for i in graph:
    # 리스트를 개별적으로 출력할 수 있게 * 붙여줌
    print(*i)

# 1부터 찾아서 츨력
print(new_x + 1, new_y + 1)
