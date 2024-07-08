# 홀수인 자연수 N이 주어지면, 다음과 같이 1부터 N제곱 까지의 자연수를 달팽이 모양으로 N * N늬 표에 채울 수 있다.
# N이 주어졌을때 이러한 표를 출력하는 프로그램을 작성하시오,
# 또한 N제곱 이하의 자연수가 하나 주어졌을 때, 그 좌표도 함께 출력하시오.
# 예를 들어 N = 5 인 경우 6의 좌표는 (4, 3)이다.

# 입력
# 첫째 줄에 홀수인 자연수 N이 주어진다. (3 <= N <= 999)
# 둘째 줄에는 위치를 찾고자 하는 N제곱 이하의 자연수가하나 주어진다.

# 출력
# N개의 줄에 걸쳐 표를 출력한다. 각줄에 N개의 자연수를 한 칸씩 띄워서 출력하면 되며, 자리수를 맞출 필요가 없다. 
# N + 1번재 줄에는 입력받은 자연수의 좌표를 나타내는 두 정수를 한 칸 띄워서 출력한다.
import sys
sys.stdin = open('week18/1913/1913.txt')
input = sys.stdin.readline

def snail(start):
    num = start
    x, y = 0, 0

    delta = [(1, 0),(0, 1), (-1, 0), (0, -1)] # 아래, 오른쪽, 위, 왼쪽
    direction = 0
    while num > 0:
        graph[x][y] = num
        num -= 1
        if num == 0:
            break
        else:
            dx, dy = delta[direction]
            # print("현재 좌표",dx,dy)
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < N and graph[nx][ny] == 0:
                x, y = nx, ny
                # print("다음 좌표",x,y)
            else:
                direction = (direction + 1) % 4
                dx, dy = delta[direction]
                nx, ny = x + dx, y + dy
                x, y = nx, ny
                continue

N = int(input())
num = int(input())

graph = [[0] * N for _ in range(N)]

start_num = N * N

# print(start_num)
snail(start_num)

for i in range(N):
    for j in range(N):
        print(graph[i][j], end = " ")
    print()

for i in range(N):
    for j in range(N):
        if graph[i][j] == num:
            print(i+1, j+1)
            break


