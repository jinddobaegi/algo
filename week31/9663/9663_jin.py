from sys import stdin

input = stdin.readline

N = int(input())


def solution(row):  # row: 행 번호
    global res
    if row == N:
        res += 1
        return

    else:
        for col in range(N):  # col: 열 번호
            # 1) col열 사용한 적 있는지
            # 2) 우상향 대각선 확인
            # 3) 우하향 대각선 확인
            if v1[col] == 0 and v2[row+col] == 0 and v3[row-col] == 0:
                v1[col] = v2[row+col] = v3[row-col] = 1
                solution(row+1)
                v1[col] = v2[row+col] = v3[row-col] = 0


res = 0
v1 = [0] * N      # 열 사용 여부
v2 = [0] * (N*2)  # y = x
v3 = [0] * (N*2)  # y = -x
solution(0)
print(res)


# 시간 초과
# res = 0
# dr = [-1, -1]
# dc = [1, -1]
#
# visited_c = [0] * N
#
# # 위, 왼쪽, 좌상, 우상 방향에 1이 있는지 확인하는 합수
# def check(r, c):
#     if visited_c[c]:
#         return False
#
#     for k in range(2):  # 방향 탐색
#         for m in range(1, N):  # 뻗어나가며 확인
#             nr = r + dr[k]*m
#             nc = c + dc[k]*m
#             if not (0 <= nr < N and 0 <= nc < N):
#                 break
#
#             if arr[nr][nc] == 1:  # 놓았던 거 있으면 컷
#                 return False
#
#     return True
#
#
# # 퀸을 놓는 함수
# def solution(r, c, cnt):
#     global res
#
#     if cnt == 0:
#         res += 1
#         return
#
#     if c > N-1:
#         solution(r+1, 0, cnt)
#         return
#
#     if r > N-1:
#         return
#
#     # 놓을 수 있는 경우
#     if check(r, c):
#         # 놓는다
#         arr[r][c] = 1
#         visited_c[c] = 1
#         solution(r+1, 0, cnt-1)
#         visited_c[c] = 0
#
#     # 가능하든 말든 관계 없이 그냥 안 놓는다
#     arr[r][c] = 0
#     solution(r, c+1, cnt)
#
#
# solution(0, 0, N)
# print(res)