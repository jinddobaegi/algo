import sys
sys.stdin = open('input.txt')

def check1(i, j):
    this_sum = 0
    if i + a <= N and j + b + c <= M:
        for row in range(i, i + a):
            for col in range(j, j + b + c):
                this_sum += area[row][col]
        return this_sum
    return None

def check2(i, j):
    this_sum = 0
    if i + a + b <= N and j + c <= M:
        for row in range(i, i + a):
            for col in range(j, j + c):
                this_sum += area[row][col]
        if j + c + a <= M:
            for row in range(i + a, i + a + b):
                for col in range(j + c, j + c + a):
                    this_sum += area[row][col]
            return this_sum
    return None

def check3(i, j):
    this_sum = 0
    if i + a + c <= N and j + b <= M:
        for row in range(i, i + a):
            for col in range(j, j + b):
                this_sum += area[row][col]
        if j + b + a <= M:
            for row in range(i + a, i + a + c):
                for col in range(j + b, j + b + a):
                    this_sum += area[row][col]
            return this_sum
    return None


N, M = map(int, input().split()) # 세로, 가로
a, b, c = map(int, input().split()) # 차와 캠핑카의 너비, 차의길이, 캠핑카의 길이
area = [list(map(int, input().split())) for _ in range(N)]

min_check1 = float('inf')
for i in range(N):
    for j in range(M):
        x = check1(i, j)
        if x is not None:
            min_check1 = min(min_check1, x)

min_check2 = float('inf')
for i in range(N):
    for j in range(M):
        x = check2(i, j)
        if x is not None:
            min_check2 = min(min_check2, x)

min_check3 = float('inf')
for i in range(N):
    for j in range(M):
        x = check3(i, j)
        if x is not None:
            min_check3 = min(min_check3, x)

ans = min(min_check1, min_check2, min_check3)
print(ans)

# 파이파이만 통과 쌩노가다

