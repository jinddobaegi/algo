import sys
input = sys.stdin.readline
# sys.stdin = open('input.txt')
sys.setrecursionlimit(10**6)
n = int(input())

# 대각선탐색
def con(x):
    for i in range(x):
        if row[x] == row[i] or abs(row[x] - row[i]) == abs(x-i):
            return False

    return True

row = [0] * n
# row의 값은 해당 행에서 퀸이 위치한 열
# row = [0, 0, 1, 0]이면
# 체스판에서 2번째 행, 1번째 열에 퀸이 있다는 뜻
ans = 0
def sol(x):
    global ans
    if x == n:
        ans += 1
        return

    # n= 4 일때
    for i in range(n):  # i = 0, 1, 2, 3
        row[x] = i # [x, i]위치에 퀸 놓기
        # row[0] = 0 => 0,0에 퀸 놓기
        if con(x):
            sol(x+1)

sol(0)
print(ans)
