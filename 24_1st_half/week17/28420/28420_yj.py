# 시간 초과 코드
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
a, b, c = map(int, input().split())  # 차와 캠핑카 넓이 a, 차의 길이 b, 캠핑카 길이 c
arr = [list(map(int, input().split())) for _ in range(N)]
INF = int(1e9)
min_sum = INF

# 일자 배치
def car1(i, j):
    if i + a > N or j + b + c > M:
        return INF
    w_sum = 0
    for k in range(i, i + a):
        for l in range(j, j + b + c):
            w_sum += arr[k][l]
    return w_sum

# 왼쪽 캠핑카, 오른쪽 차
def car2(i, j):
    if i + a + b > N or j + c + a > M:
        return INF
    w_sum = 0
    # 캠핑카
    for k in range(i, i + a):
        for l in range(j, j + c):
            w_sum += arr[k][l]
    # 차
    for k in range(i + a, i + a + b):
        for l in range(j + c, j + c + a):
            w_sum += arr[k][l]
    return w_sum

# 왼쪽 차, 오른쪽 캠핑카
def car3(i, j):
    if i + a + c > N or j + b + a > M:
        return INF
    w_sum = 0
    # 차
    for k in range(i, i + a):
        for l in range(j, j + b):
            w_sum += arr[k][l]
    # 캠핑카
    for k in range(i + a, i + a + c):
        for l in range(j + b, j + b + a):
            w_sum += arr[k][l]
    return w_sum

for i in range(N):
    for j in range(M):
        min_sum = min(min_sum, car1(i, j), car2(i, j), car3(i, j))

print(min_sum)