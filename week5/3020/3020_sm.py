# 개똥벌레
# 골드 5

import sys

# 저 이거 틀렸어요..
# 동굴 길이 / 높이
N, H = map(int, input().split())

s = []
j = []
# 출력할 값
min_v = N
cnt = 0

for i in range(N):
    if i % 2 == 0:
        s.append(int(input()))
    else:
        j.append(int(input()))

for i in range(H-1, 0, -1):
    s[i] += s[i+1]
    j[i] += j[i+1]

for i in range(1, H+1):

    if min_v > (s[i] + j[H-i+1]):
        min_v = (s[i] + j[H-i+1])
        cnt = 1
    elif min_v == (s[i] + j[H-i+1]):
        cnt += 1

print(min_v, cnt)

# 저 이거 틀렸어요..