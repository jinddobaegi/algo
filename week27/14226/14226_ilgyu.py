import sys
sys.stdin = open('input.txt')
from collections import deque

s = int(input())

visited = [[False] * (1001) for _ in range(1001)]

def sol():
    q = deque()
    q.append([0, 1, 0])
    visited[0][1] = True # (클립보드, 스크린) 이모티콘 경우의 수 방문여부

    while q:
        clip, screen, cnt = q.popleft()

        if screen == s:
            return cnt

        for k in range(3):

            if k == 0: # 클립보드에 복사
                next_clip, next_screen = screen, screen

            elif k == 1: # 화면에 붙여넣기
                next_clip, next_screen = clip, screen + clip

            else: # 화면 -1
                next_clip, next_screen = clip, screen - 1

            if next_clip > 1000 or next_clip < 0 or next_screen > 1000 or next_screen < 0 or visited[next_clip][next_screen]:
                continue

            visited[next_clip][next_screen] = True
            q.append([next_clip, next_screen, cnt + 1])
ans = sol()
print(ans)

# 시간초과
# import sys
# input = sys.stdin.readline
# from collections import deque
#
# s = int(input())
#
# # 1. 화면에 있는 이모티콘을 모두 복사해서 클립보드에 저장한다.
# # 2. 클립보드에 있는 모든 이모티콘을 화면에 붙여넣기 한다.
# # 3. 화면에 있는 이모티콘 중 하나를 삭제한다.
#
# # s = 4
# # 맨처음 1개의 이모티콘
# # 1 시행 (누적시간 1초, 클립보드 1개, 화면 1개)
# # 2 시행 (누적시간 2초, 클립보드 0개, 화면 2개)
# # 1 시행 (누적시간 3초, 클립보드 2개, 화면 2개)
# # 2 시행 (누적시간 4초, 클립보드 0개, 화면 4개)
# # 정답: 4초
# # 숨바꼭질이랑 비슷한듯
# visited = [False] * (2001)
# # visited[2] = 화면수 2에 도착하는데 걸린 시간
# def sol(c, sc):
#     q = deque()
#     q.append([c, sc, 0])
#             # 클립보드, 화면, 시간
#     visited[sc] = True
#     while q:
#         clip, screen, cnt = q.popleft()
#
#         if screen == s:
#             return cnt
#
#         # 선택할 수 있는 거
#         # 클립보드에 복사, 화면에 넣기, 화면에서 1개 제거
#         for next in (["복사", "붙여넣기", "제거"]):
#             # print(next)
#             if next == "복사": # 클립보드에 복사
#                 if [clip + screen, screen, cnt + 1] not in q:
#                     q.append([clip + screen, screen, cnt + 1])
#             elif next == "붙여넣기": # 스크린에 붙여넣기
#                 if visited[screen + clip]:
#                     continue
#                 if [clip, screen + clip, cnt + 1] not in q:
#                     q.append([0, screen + clip, cnt + 1])
#             elif next == "제거":
#                 if visited[screen -1] or screen - 1 < 0:
#                     continue
#                 if [clip, screen - 1, cnt + 1] not in q:
#                     q.append([clip, screen - 1, cnt + 1])
#             # print(q)
# ans = sol(0, 1)
# print(ans)
