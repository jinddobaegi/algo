from sys import stdin

input = stdin.readline


def get_permutations(x):
    if not dp[x]:
        dp[x] = get_permutations(x - 1) + get_permutations(x - 2)

    return dp[x]


N = int(input())
M = int(input())
vips = None
if M:
    vips = list(int(input()) for _ in range(M))
    vips = tuple(vips + [N+1])

dp = [0] * (N + 1)
dp[0], dp[1] = 1, 1

# vip 좌석은 없을 수도 있음
res = 1
if not M:
    print(get_permutations(N))
elif M in (N, N-1):
    print(1)
else:
    v1 = 0
    for v2 in vips:
        res *= get_permutations(v2 - v1 - 1)
        v1 = v2

    print(res)