# 나무 판자의 크기는 1
# 방은 직사각형
# - 와 |로 이루어진 바닥장식 모양이 주어짐
# -x2 인접해있고 같은 행에 있다면? 두개는 같은 나무 판자이고
# |x2 인접해잇고 같은 열에 있다면? 두개는 같은 나무 판자이다.

N, M = map(int, input().split())
arr = [list(input()) for _ in range(N)]
cnt = N * M

for a in range(N): # 세로
    for b in range(M): # 가로
        if (arr[a][b] == '-' and b < M - 1 and arr[a][b + 1] == '-'):
            cnt -= 1
        if (arr[a][b] == '|' and a < N - 1 and arr[a + 1][b] == '|'):
            cnt -= 1
print(cnt)