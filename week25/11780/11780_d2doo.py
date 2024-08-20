# 플로이드 2
# 플로이드 워셜 알고리즘
# 모든 노드 냅다 탐색하며 2차원 테이블을 만들어 최단거리 정보를 저장한다.
# 처음엔 인접한 노드만, 그 다음은 노드 1을 거쳐서, 그 다음은 노드2를 거쳐서, 그 다음은 노드 3을 거쳐서...

# 출력 설명
# 1 : 모든 도시에 대한 최소 비용
# 2 : n x n 자리에 [거치는 도시의 개수(3), 거치는 도시(1), 거치는 도시(2), 거치는 도시(3)]
import sys
sys.stdin = open("week25/11780/11780.txt")

n = int(input()) # 도시의 수
m = int(input()) # 버스의 수

INF = int(1e9)

# 최단 거리 테이블
dist = [[INF] * (n + 1) for _ in range(n + 1)]
next_node = [[0] * (n + 1) for _ in range(n + 1)]

# 자기 자신으로 가는 비용은 0으로 초기화
for i in range(1, n + 1):
    dist[i][i] = 0

# bus_info = [[] for _ in range(n + 1)] # 버스 시작점, 도착점, 비용 정보
for _ in range(m):
    start, end, cost = map(int, input().split())
    # bus_info[start].append((end, cost))
    if cost < dist[start][end]:  # 더 작은 비용이 있으면 갱신
        dist[start][end] = cost
        next_node[start][end] = end

# 거쳤던 노드 저장
for k in range(1, n + 1): # 거쳐야 하는 노드를 순차적으로 바꿔준다
    for start in range(1, n + 1): # 시작지점 에서
        for end in range(1, n + 1): # 도착지점 까지 가는 길을 갱신한다
            '''
            현재 저장된 a에서 b로 가는 최소비용과, k 노드를 지나쳤을 때의 값을 비교
            dist[start][end] = min(dist[start][end], dist[start][k] + dist[k][end])
            '''
            if dist[start][k] + dist[k][end] < dist[start][end]:
                dist[start][end] = dist[start][k] + dist[k][end]
                next_node[start][end] = next_node[start][k] + k + next_node[k][end]


for start in range(1, n + 1):
    for end in range(1, n + 1):
        print(dist[start][end] if dist[start][end] != INF else 0, end = ' ')
    print()

for start in range(1, n + 1):
    for end in range(1, n + 1):
        if start == end: # 같은 애
            print(0)
        elif dist[start][end] == INF: # 도달할 수 없는 애
            print(0)
        else:
            print(len(next_node[start][end]) + 2, start, next_node, end)
