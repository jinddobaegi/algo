import sys
sys.stdin = open('input.txt')
from collections import deque
from itertools import combinations
import copy

di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

def virus_spread(i, j, copy_map):
    q = deque()
    q.append([i, j])

    while q:
        x, y = q.popleft()

        for k in range(4):
            nx, ny = x + di[k], y + dj[k]
            if 0 <= nx < n and 0 <= ny < m and copy_map[nx][ny] == 0:
                q.append([nx, ny])
                copy_map[nx][ny] = 2


n, m = map(int, input().split()) # 세로, 가로
my_map = [list(map(int, input().split())) for _ in range(n)]

# 1. 0의 좌표를 저장할 리스트
empty_spaces = []

for i in range(n):
    for j in range(m):
        if my_map[i][j] == 0:
            empty_spaces.append((i, j))

# 2. 0의 좌표들 중 3개를 선택
combi = combinations(empty_spaces, 3)
# print(list(combi))
# combi에 있는 0의 좌표의 조합을 한개씩 돌면서
# 각각의 경우 바이러스를 증식시키는 함수를 실행하고
# 최종적으로 안전영역이 몇개가되는지 매번 갱신 후 최대값 구하기
max_safe = 0
for empty in combi:
    # empty = ((1,1), (1,2), (1,3)) 이런식으로 생김
    # print(empty[0][0])
    copy_map = copy.deepcopy(my_map)

    # 1. 벽 세우기
    for case in empty:
        x, y = case[0], case[1]
        copy_map[x][y] = 1

    # 2. 바이러스 찾아서 증식시키기
    for i in range(n):
        for j in range(m):
            if copy_map[i][j] == 2:
                virus_spread(i, j, copy_map)

    # 3. 남는 0의 개수 카운팅
    ans = 0
    for i in range(n):
        for j in range(m):
            if copy_map[i][j] == 0:
                ans += 1
    max_safe = max(ans, max_safe)

print(max_safe)

