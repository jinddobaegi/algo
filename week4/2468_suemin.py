# 안전 영역
# 실버 1

import sys

N = int(input())
lst = [list(map(int, input().split())) for _ in range(N)]

di = [0, 0, -1, 1]
dj = [-1, 1, 0, 0]

