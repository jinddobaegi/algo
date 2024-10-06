from sys import stdin

input = stdin.readline

N = int(input())
arr = list([0] * N for _ in range(N))
res = 0
dr = [-1, -1]
dc = [1, -1]

visited_c = [0] * N

# 위, 왼쪽, 좌상, 우상 방향에 1이 있는지 확인하는 합수
def check(r, c):
    if visited_c[c]:
        return False

    for k in range(2):  # 방향 탐색
        for m in range(1, N):  # 뻗어나가며 확인
            nr = r + dr[k]*m
            nc = c + dc[k]*m
            if not (0 <= nr < N and 0 <= nc < N):
                break

            if arr[nr][nc] == 1:  # 놓았던 거 있으면 컷
                return False

    return True


# 퀸을 놓는 함수
def solution(r, c, cnt):
    global res

    if cnt == 0:
        res += 1
        return

    if c > N-1:
        solution(r+1, 0, cnt)
        return

    if r > N-1:
        return

    # 놓을 수 있는 경우
    if check(r, c):
        # 놓는다
        arr[r][c] = 1
        visited_c[c] = 1
        solution(r+1, 0, cnt-1)
        visited_c[c] = 0

    # 가능하든 말든 관계 없이 그냥 안 놓는다
    arr[r][c] = 0
    solution(r, c+1, cnt)


solution(0, 0, N)
print(res)