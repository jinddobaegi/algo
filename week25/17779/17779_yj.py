N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

def cal(x, y, d1, d2):
    cnt = [0] * 5
    lst = [[0 for _ in range(N+1)] for _ in range(N+1)]

    # 경계선 그리기
    for i in range(d1+1):
        lst[x+i][y-i] = 5
        lst[x+d2+i][y+d2-i] = 5

    for i in range(d2+1):
        lst[x+i][y+i] = 5
        lst[x+d1+i][y-d1+i] = 5

    # 5번 선거구 내부 채우기
    for i in range(x+1, x+d1+d2):
        temp = False
        for j in range(1, N+1):
            if lst[i][j] == 5:
                temp = not temp
            if temp:
                lst[i][j] = 5

    # 나머지 채우기
    for i in range(1, N+1):
        for j in range(1, N+1):
            if lst[i][j] == 5:
                cnt[4] += arr[i-1][j-1]
            elif i < x + d1 and j <= y:
                lst[i][j] = 1
                cnt[0] += arr[i-1][j-1]
            elif i <= x + d2 and y < j <= N:
                lst[i][j] = 2
                cnt[1] += arr[i-1][j-1]
            elif x + d1 <= i <= N and j < y - d1 + d2:
                lst[i][j] = 3
                cnt[2] += arr[i-1][j-1]
            elif x + d2 < i <= N and y - d1 + d2 <= j <= N:
                lst[i][j] = 4
                cnt[3] += arr[i-1][j-1]

    return max(cnt) - min(cnt)

min_d = int(1e9)
for x in range(1, N+1):
    for y in range(1, N+1):
        for d1 in range(1, N+1):
            for d2 in range(1, N+1):
                if x + d1 + d2 <= N and 1 <= y - d1 and y + d2 <= N:
                    min_d = min(min_d, cal(x, y, d1, d2))

print(min_d)