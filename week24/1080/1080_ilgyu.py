import sys
sys.stdin = open('input.txt')

n, m = map(int, input().split())
A = [list(map(int, input())) for _ in range(n)]
B = [list(map(int, input())) for _ in range(n)]
# for x in A:
#     print(x)
#
# for x in B:
#     print(x)
def sol(i, j): # 뒤집는 함수
    global ans
    if 0 <= i + 2 <= n and 0 <= j + 2 <= m:
        for x in range(i, i+3):
            for y in range(j, j+3):
                A[x][y] = 1 - A[x][y]
    # 이런 경우때문에 뒤집기함수 시행하는 부분에서 범위검사해줘야함
    # 0000
    # 0000
    # 0000
    # 0000

    # 0001
    # 0001
    # 0001
    # 0001
    else:
        ans -= 1
        # 함수끝나면 ans += 1 하는데
        # 뒤집기 안하는 경우에도 카운팅되니까 돌려주기


if n < 3 or m < 3:
    if A == B:
        print(0)
    else:
        print(-1)
else:
    ans = 0
    for i in range(n-2):
        for j in range(m-2):
            if A[i][j] != B[i][j]:
                sol(i, j)
                ans += 1
    # 연산 다 해보고 못 만들때
    if A == B:
        print(ans)
    else:
        print(-1)



