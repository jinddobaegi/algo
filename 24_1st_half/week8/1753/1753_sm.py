import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

import heapq

# 문제
# 첫째 줄에 정점의 개수 V와 간선의 개수 E가 주어진다. (1 ≤ V ≤ 20,000, 1 ≤ E ≤ 300,000)
# 모든 정점에는 1부터 V까지 번호가 매겨져 있다고 가정한다.
# 둘째 줄에는 시작 정점의 번호 K(1 ≤ K ≤ V)가 주어진다.
# 셋째 줄부터 E개의 줄에 걸쳐 각 간선을 나타내는 세 개의 정수 (u, v, w)가 순서대로 주어진다.
# 이는 u에서 v로 가는 가중치 w인 간선이 존재한다는 뜻이다. u와 v는 서로 다르며 w는 10 이하의 자연수이다.
# 서로 다른 두 정점 사이에 여러 개의 간선이 존재할 수도 있음

# 경로 없으면 INF 출력


# heap 처음 써봐서 찾아본 heap 함수
# heapq.heappush(heap, item) : item을 heap에 추가
# heapq.heappop(heap) : heap에서 가장 작은 원소를 pop & 리턴. 비어 있는 경우 IndexError가 호출됨.
# heapq.heapify(x) : 리스트 x를 즉각적으로 heap으로 변환함 (in linear time, O(N) )

n, m = map(int, input().split())    # 정점  간선
k = int(input())      # 시작 정점
# 무한
INF = int(1e9)

# 그래프 초기화
graph = [[] * (n+1) for _ in range(n+1)]
# 최단 거리 테이블을 모두 무한으로 초기화
distance = [INF] * (n+1)

# 간선 가져오기
for _ in range(m):
    a, b, c = map(int, input().split())
    # a->b : c비용
    graph[a].append((b, c))

def dijkstra(start):
    q = []
    # 시작 노드로 가는 걸 0으로 설정 -> 큐에 넣어
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        # 가장 짧은 노드 가져와
        dist, now = heapq.heappop(q)
        # 현재 노드가 이미 처리된 적이 있는 노드면 무시
        if distance[now] < dist:
            continue
        # 인접 노드확인
        for i in graph[now]:
            cost = dist + i[1]
            # 현재 노드 ->  다른 노드로 이동하는 거리가 더 >> 짧은 경우 <<
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

# 실행
dijkstra(k)

# 최단거리 출력 ㄱ
for i in range(1, n+1):
    if distance[i] == INF:
        print("INF")
    else:
        print(distance[i])