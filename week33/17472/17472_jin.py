from collections import deque
from sys import stdin

input = stdin.readline

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
visited = [[0] * m for _ in range(n)]
delta = [(0, 1), (1, 0), (0, -1), (-1, 0)]
land_arr = []  # 원소: (i, j, ij의 섬 번호)

# 섬 구분 + 좌표 구하기, BFS
land_num = 0
for i in range(n):
    for j in range(m):
        if arr[i][j] == 1 and not visited[i][j]:
            land_num += 1
            q = deque([(i, j)])
            visited[i][j] = 1
            arr[i][j] = land_num
            land_arr.append((i, j, land_num))
            while q:
                x, y = q.popleft()
                for a, b in delta:
                    dx = x + a
                    dy = y + b
                    if n > dx >= 0 and m > dy >= 0 and not visited[dx][dy] and arr[dx][dy]:
                        q.append((dx, dy))
                        visited[dx][dy] = 1
                        arr[dx][dy] = land_num
                        land_arr.append((dx, dy, land_num))

# 다리 제작
bridges = []  # 원소: (섬 사이 거리, 섬1, 섬2)
for x, y, land_cur in land_arr:  # 섬이 있는 모든 좌표를 돌면서
    for a, b in delta:
        dist = 0
        dx = x + a
        dy = y + b
        while True:
            if n > dx >= 0 and m > dy >= 0:
                land_next = arr[dx][dy]  # 주변 좌표 확인
                # 같은 섬
                if land_cur == land_next:
                    break
                # 바다 위 => 다리 길이 +1
                if not land_next:
                    # 가던 방향으로 진행
                    dx += a
                    dy += b
                    dist += 1
                    continue
                # 다른 섬 도달
                if dist < 2:  # 다리가 짧음
                    break

                # 다른 섬 도달 + 다리 길이 충분
                bridges.append((dist, land_cur, land_next))  # 두 섬 사이 가능한 모든 다리의 길이를 담을 것임
                break

            else:
                break

bridges.sort(reverse=True)  # pop으로 짧은 걸 뽑기 위해, 거리 긴 순으로 정렬


def union(x, y):
    global parents

    x = find(x)
    y = find(y)
    parents[y] = x


def find(k):
    global parents

    if k != parents[k]:
        parents[k] = find(parents[k])
    return parents[k]


# Kruskal
def kruskal(bridge_cnt, bridges):
    global parents

    res = 0
    while bridge_cnt and bridges:
        w, a, b = bridges.pop()
        if find(a) != find(b):
            union(a, b)
            res += w
            bridge_cnt -= 1

    if not bridge_cnt:
        return res
    else:
        return -1


parents = [i for i in range(land_num + 1)]
print(kruskal(land_num-1, bridges))