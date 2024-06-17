# 카더가든

# ㅡ 자 모양
def first():
    global ans
    sum_v = 0
    for i in range(N):
        for j in range(M - b - c + 1):
            sum_v += sum(maps[i][j : j + b + c])
    ans = min(ans, sum_v)
    print(f'a={ans}')

# ㄱ자 모양1(차가 ㅡ, 캠핑카가 ㅣ)
def second():
    global ans
    for i in range(N - b - c + 1):
        for j in range(M - a):
            sum_v = 0
            # 차가 차지하는 부분
            for k in range(b):
                sum_v += maps[i + k][j]
            # 캠핑카가 차지하는 부분
            for k in range(c):
                sum_v += maps[i + k][j + b]
            ans = min(ans, sum_v)

# ㄱ자 모양2(차가 ㅣ, 캠핑카가 ㅡ)
def third():
    global ans
    for i in range(N - b):
        for j in range(M - a - c + 1):
            sum_v = 0
            # 캠핑카가 차지하는 부분
            for k in range(c):
                sum_v += maps[i + k][j + a]
            # 차가 차지하는 부분
            for k in range(b):
                sum_v += maps[i + c][j + k:j + k + a]
            ans = min(ans, sum_v)


N, M = map(int, input().split())
a, b, c = map(int, input().split()) # a: 너비, b: 차 길이, c: 캠핑카 길이
maps = [list(map(int, input().split())) for _ in range(N)]
ans = 1e7

first()
second()
third()

print(ans)