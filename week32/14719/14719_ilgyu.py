# import sys
# sys.stdin = open('input.txt')
#
# h, w = map(int, input().split())
# heights = list(map(int, input().split()))

# # 전체 지역은
# area = [[-1] * w for _ in range(h)]
#
# # area에 -1은 빈 공간, 1은 블록, 0은 빗물로 표시
# # print(heights)
# for k in range(w):
#     for i in range(heights[k]):
#         area[i][k] = 1
# #
# # for m in area:
# #     print(m)
# # 뒤집어서 보면 됨
#
# # 어떤 기준으로 빗물을 채울건지
# def check(x, y):
#     left = 0 #왼쪽에 있는 블록
#     right = 0 # 오른쪽에 있는 블록
#
#     for k in range(w):
#         if area[x][k] == 1:
#             if k < y:
#                 left += 1
#             elif k > y:
#                 right += 1
#     if left >= 1 and right >= 1:
#         return True
#     else:
#         return False
#
# ans = 0
# for i in range(h):
#     for j in range(w):
#         if area[i][j] == -1:
#             if check(i, j):
#                 ans += 1
#
# print(ans)

import sys
input = sys.stdin.readline

h, w = map(int, input().split())
heights = list(map(int, input().split()))

ans = 0

for i in range(1, w-1):
    left = max(heights[:i])
    right = max(heights[i+1:])

    s = min(left, right)
    if heights[i] <= s:
        ans += s - heights[i]

print(ans)






