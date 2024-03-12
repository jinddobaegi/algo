import sys
sys.stdin = open('input.txt')
from collections import deque

di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

# 근데 순서가 물에 잠기는지 아닌지 먼저 판단하고
# 덩어리 몇개인지 확인해야 함
def check(i, j, sink, visited): # 연결된 지점들 확인
    q = deque()
    start = [i, j]
    q.append(start)
    visited[i][j] = True

    while q:
        x, y = q.popleft()
        for k in range(4):
            nx, ny = x + di[k], y + dj[k]
            if 0 <= nx < N and 0 <= ny < N and visited[nx][ny] == False and sink[nx][ny] == False:
                visited[nx][ny] = True # 방문처리
                q.append([nx, ny])

def safe_area(water): # 높이마다 잠김여부, 방문여부를 매번 새로 만들어줘야함
    sink = [[False] * N for _ in range(N)] # 잠겼는지 확인하는 용도
    visited = [[False] * N for _ in range(N)] # 인접행렬 조사하면서 확인하는 용도

    # 높이별로 잠기는지 확인
    for i in range(N):
        for j in range(N):
            if area[i][j] <= water:
                sink[i][j] = True # True면 잠긴 상태

    # 잠김 여부 표시한 리스트(sink)에서 덩어리 체크
    res = 0
    for i in range(N):
        for j in range(N):
            if sink[i][j] == False and visited[i][j] == False: # 돌면서 잠김 여부 확인해서 안 잠겨 있으면 덩어리들 확인
                check(i, j, sink, visited)
                res += 1
    return res

N = int(input()) # 지역의 수
area = [list(map(int, input().split())) for _ in range(N)] # 높이정보

# 얘는 잠김여부와 별개로 맞닿아 있는지 확인하는 용도?
# 생각해보니까 visited도 함수 안에서 매번 새로 해줘야함
max_cnt = 0
# 높이는 1이상 100이하
# 근데 이게 지역의 높이임 물의 높이임?
# 1~100이 지역의 높이이면 물은 1~100까지만 확인하면 됨 어차피 101부턴 다 잠기니까

# 물의 높이가 0인경우를 고려해줘야함
for water in range(0, 101):
    cnt = safe_area(water)
    max_cnt = max(max_cnt, cnt)

print(max_cnt)