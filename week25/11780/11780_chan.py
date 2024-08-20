import sys
sys.stdin = open("week25/11780/11780.txt")
input = sys.stdin.readline

N = int(input())
M = int(input())

# 무한대 값으로 초기화
city_map = [[float("inf")] * N for _ in range(N)]
path = [[-1] * N for _ in range(N)]

# 자기 자신으로 가는 경로는 0으로 설정
for i in range(N):
    city_map[i][i] = 0

# 간선 정보 입력
for _ in range(M):
    a, b, c = map(int, input().split())
    a -= 1
    b -= 1
    if city_map[a][b] > c:
        city_map[a][b] = c
        path[a][b] = a  # 경로 초기화

# 플로이드-워셜 알고리즘 적용
for k in range(N):
    for i in range(N):
        for j in range(N):
            if city_map[i][j] > city_map[i][k] + city_map[k][j]:
                city_map[i][j] = city_map[i][k] + city_map[k][j]
                path[i][j] = path[k][j]  # 경로 갱신
                # print(path)

# 최단 경로 비용 출력
for i in range(N):
    for j in range(N):
        if city_map[i][j] == float("inf"):
            print(0, end=" ")
        else:
            print(city_map[i][j], end=" ")
    print()

# 경로 출력 함수
def get_path(i, j):
    if path[i][j] == -1:
        return []
    route = []
    while j != i:
        route.append(j + 1)
        j = path[i][j]
    route.append(i + 1)
    route.reverse()
    return route

# 경로 정보 출력
for i in range(N):
    for j in range(N):
        if city_map[i][j] == float("inf") or i == j:
            print(0)
        else:
            route = get_path(i, j)
            print(len(route), " ".join(map(str, route)))