# 아기상어
# 골드 3

# bfs로 풀자

'''
상어 초기 위치 찬고
어떤 물고기 먹을 지 체크를 bfs를 통해 탐색
상어가 그 물고기 먹으러 이동하고
이걸 반복해
'''


# 이거 잘 이해가 안 되네요 설명 구다사이...


# import heapq
# from collections import deque
# import sys
# input = sys.stdin.readline
#
# def bfs(r, c, shark_size):
#     visited = [[0] * n for _ in range(n)]
#     q = deque()
#     q.append([r, c, 0])
#     eat = []  # 먹을 수 있는 고기 리스트
#
#     if not visited[r][c]:
#         visited[r][c] = 1
#
#     while q:
#         x, y, dist = q.popleft()
#
#         for i in range(4):
#             nx, ny = x + dx[i], y + dy[i]
#
#             if 0 <= nx < n and 0 <= ny < n:
#                 if not visited[nx][ny]:
#                     visited[nx][ny] = 1
#
#                     if board[nx][ny] == 0 or board[nx][ny] == shark_size:
#                         q.append((nx, ny, dist+1))
#
#                     elif board[nx][ny] != 0 and board[nx][ny] < shark_size:
#                         heapq.heappush(eat, (dist + 1, nx, ny))
#
#     if eat:
#         return [eat[0][1], eat[0][2], eat[0][0]]
#
#     # 먹을 수 있는 물고기 없으면 종료시켜
#     else:
#         return
#
#
#
# n = int(input())
# board = []
#
# for _ in range(n):
#     board.append([map(int, input().split())])
#
#
# # 상어 크기
# shark_size = 2
# exp = 0
#
# res = 0
# dx = [-1, 1, 0, 0]
# dy = [0, 0, 1, -1]
#
# # 1. 아기상어 초기 위치 찾기
# for r in range(n):
#     for c in range(n):
#         if board[r][c] == 9:
#             board[r][c] = 0
#             shark_r, shark_c = r, c #상어의 현재 위치 정보 저장
#             break
#
#
# # 2. 어떤 물고기 먹을 수 있는지 탐색
# while True:
#     fish_info = bfs(shark_r, shark_c, shark_size)
#
#     if fish_info:
#         shark_r, shark_c, time = fish_info
#         board[shark_r][shark_c] = 0
#         exp += 1
#         res += time
#
#         # 4. 자기 크기랑 같은 물고기 먹을 때마다 아기상어 크기 증가
#         if exp == shark_size:
#             shark_size += 1
#             exp = 0
#
#     # 5. 엄마 상어에게 도움 요청하면 종료
#     else:
#         print(res)
#         break

