# 검색했는데 정확하게 이해를 못 함

import sys
input = sys.stdin.readline

n, h = map(int, input().split(" "))

# 누적합 이용
lines = [0] * h

for i in range(n):
    high = int(input())
    # 석순
    if i % 2 == 0:
        lines[h - high] += 1
    # 종유석
    else:
        lines[0] += 1
        lines[high] -= 1
        
# 누적합
for i in range(1, h):
    lines[i] += lines[i - 1]
    
# 최소값 체크 및 최소값 갯수 체크
count = 0
low = min(lines)
for i in lines:
    if i == low:
        count += 1
        
print(low, count)


# 시간 초과 ㅠㅠ
# N, H = map(int, input().split())
# arr = [0] * H
# sum_m = 0

# for i in range(N):
#     M = int(input())

#     if i % 2 == 0:
#         for j in range(H-1, H-M-1, -1):
#             arr[j] += 1
#     else:
#         for j in range(0, M):
#             arr[j] += 1

# for i in arr:
#     if i == min(arr):
#         sum_m += 1

# print(min(arr), sum_m)