import sys
sys.stdin = open('input.txt')

V, E = map(int, input().split())

# 크루스칼 알고리즘 : 모든 정점을 최소한의 비용으로 연결

# 1. 부모 테이블상에서 부모를 자기 자신으로 초기화
parent = [0] * (V+1)

# 2. 부모 테이블에서 자기자신을 대표노드로 설정
for i in range(1, V+1):
    parent[i] = i
# print(parent)

# 3. 간선을 담을 리스트와 최소비용을 담을 변수 설정
graph = [] # 간선정보
results = 0 # 비용정보
for _ in range(E):
    s, e, cost = map(int, input().split())
    graph.append((cost, s, e)) # 비용순 정렬을 위해 cost를 튜플의 첫번째로
# print(graph)

# 4. 간선을 오름차순(비용기준)으로 정렬
graph.sort()

# 5.  find, union 함수 정의
def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]

def union(parent, x, y):
    x = find(parent, x)
    y = find(parent, y)
    ## 이 if문이 잘 이해가 안됨
    if x < y:  # 작은 쪽이 부모가 된다. (한 집합 관계라서 부모가 따로 있는 건 아님)
        parent[y] = x
    else:
        parent[x] = y

def same_parent(a, b):
    return find(parent, a) == find(parent, b)

ans = 0
for cost, a, b in graph:
    # cost가 작은 edge부터 하나씩 추가해가면서 같은 부모를 공유하지 않을 때(사이클 없을 때)만 확정
    if not same_parent(a, b):
        union(parent, a, b)
        ans += cost

print(ans)
