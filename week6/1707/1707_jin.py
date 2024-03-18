from sys import stdin
from collections import deque

input = stdin.readline

# 정점의 집합을 둘로 분할
# 각 집합에 속한 정점끼리
# 서로 인접하지 않도록 분할할 수 있다 -> 이분 그래프

# 그러면, 한 정점에서
# 탐색 가능한 모든 정점, 즉 인접 정점이
# 나와 다른 집합에 속해야 함
# 그럼 현재 정점이 속한 집합도 알아야 하고
# 인접 노드의 방문 여부와 집합 일치 여부를 확인해야 함

K = int(input())

for tc in range(K):
    V, E = map(int, input().split())
    # 정점은 1~V까지 총 V개 있음
    # 간선은 E개임
    adj_list = list([] for _ in range((V+1)))
    for _ in range(E):
        u, v = map(int, input().split())
        adj_list[v].append(u)
        adj_list[u].append(v)

    visited = [0]*(V+1)
    list_a = []
    list_b = []

    # bfs
    q = deque()
    # 항상 1번부터 시작, 1번 노드는 a에 담을 것임
    # 노드 번호와 함께 list_a/b 중 어디에 속하는지 정보 같이 넘김
    # a: 0, b: 1
    q.append((1, 0))
    visited[1] = 1
    list_a.append(1)

    # bfs 돌면서 다음 노드의 방문 여부와
    # 현재 노드와 집합 비교 할 것
    # 조건이 안 맞으면 'NO' 출력
    res = 'YES'

    while q and res == 'YES':
        v, v_num = q.popleft()

        for w in adj_list[v]:

            if not visited[w]:     # 다음 노드 미방문한 경우
                visited[w] = 1
                if v_num == 0:  # 현재 노드가 a에 속하는 경우
                    q.append((w, 1))
                    list_b.append(w)
                else:              # 현재 노드가 b에 속하는 경우
                    q.append((w, 0))
                    list_a.append(w)

            else:                  # 다음 노드를 이미 방문한 경우
                # 인접 노드가 현재 노드와 같은 집합에 있는지 확인
                # 같은 집합이면 -> 'NO'
                if (v_num and w in list_b) or (not v_num and w in list_a):
                    res = 'NO'
                    break

    print(res)