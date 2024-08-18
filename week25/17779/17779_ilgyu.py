import sys
sys.stdin = open('input.txt')

n = int(input())
arr = [[]]
for _ in range(n):
    arr.append([0] + list(map(int, input().split())))

# 1. 선거구를 나누려면 5번선구를 일단 만들어야함

# 5번 선거구의 상하좌우 가장 끝지점의 좌표를 구함
# x, y, d1, d2 만드는 방법의 수
# 기준점 (x, y)에서 n = 7, x = 0, y = 1 일 때
# 될 수 있는 d1 = 1 ,
# d2 = 1 ~ 5
# 2 <= d1 + d2 <= 6이면 됨

# x = 2, y = 5, d1 = 3, d2 = 2 일 때
# 기준점 x,y 에 대해서
# 경계선이 되는 점들을 구해보면
# 위쪽 / 모양
# x-1, y+1
# x-2, y+2
# x-3, y+3
# for k in range(1, d1+1):
#       x-k, y+k

# 위쪽 \ 모양
# x+1, y+1
# x+2, y+2
# for k in range(1, d2+1):
#       x+k, y+k

# 아래쪽 / 모양
# x+d2, y+d2 를 기준으로
# x+d2-1, y+d2+1
# x+d2-2, y+d2+2
# x+d2-3, y+d2+3
# for k in range(1, d1+1):
#           x+d2-k, y+d2+k

# 아래쪽 \ 모양
# x-d1, y+d1 기준으로
# x-d1+1, y+d1+1
# x-d1+2, y+d1+2
# for k in range(1, d2+1):
#           x-d1+k, y+d1+k

# 정리하면 총 4개를 도는데


# 이걸 어떻게 써야되지
# for k in range(1, d1+1):
#     nx, ny = x-k, y+k
#
# for k in range(1, d2+1):
#     nx, ny = x+k, y+k
#
# for k in range(1, d1+1):
#     nx, ny = x+d2-k, y+d2+k
#
# for k in range(1, d2+1):
#     nx, ny = x-d1+k, y+d1+k

# 근데 이렇게 다 구해보고 밖으로 나가는 건 없어야 함
# 이 4개의 for문을 돈 값들이 경계선 좌표들임
def sol(x,y,d1,d2):
    cnt = [0,0,0,0,0]
    f = [[0 for _ in range(n+1)] for _ in range(n+1)]

    # 경계선
    for i in range(d1+1):
        f[x+i][y-i] = 1
        f[x+d2+i][y+d2-i] = 1
    for j in range(d2+1):
        f[x+j][y+j] = 1
        f[x+d1+j][y-d1+j] = 1

    # 내부
    for i in range(x + 1, x + d1 + d2):
        flag = False
        for j in range(n + 1):
            if f[i][j] == 1:
                if flag == True:
                    flag = False
                else:
                    flag = True
            else:
                if flag == True:
                    f[i][j] = 1

    for r in range(1, n+1):
        for c in range(1, n+1):
            if 1 <= r < x+d1 and 1 <= c <= y and f[r][c] != 1:
                cnt[0] += arr[r][c]
            elif 1 <= r <= x+d2 and y < c <=n and f[r][c] != 1:
                cnt[1] += arr[r][c]
            elif x+d1 <= r <= n and 1 <= c < y-d1+d2 and f[r][c] != 1:
                cnt[2] += arr[r][c]
            elif x+d2 < r <= n and y-d1+d2 <= c <= n and f[r][c] != 1:
                cnt[3] += arr[r][c]
            elif f[r][c] == 1:
                cnt[4] += arr[r][c]

    return max(cnt) - min(cnt)

min_v = float('inf')
for x in range(1, n+1):
    for y in range(1, n+1):
        for d1 in range(1, n+1):
            for d2 in range(1, n+1):
                if 1 <= x < x+d1+d2 <= n and 1 <= y-d1 < y < y+d2 <=n:
                    min_v = min(min_v, sol(x,y,d1,d2))

print(min_v)

