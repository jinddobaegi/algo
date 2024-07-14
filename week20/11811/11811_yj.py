# arr[2][3] = 수열[2] & 수열[3] ?
# 행에 있는 모든 값 or 연산하기

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
s = [0] * N

for i in range(N):
    for j in range(N):
        if i == j:
            continue
        s[i] = s[i] | arr[i][j]

print(*s)