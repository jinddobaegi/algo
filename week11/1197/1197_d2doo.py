# 최소 스패닝 트리
# 주어진 그래프의 모든 정점들을 연결하는 부분 그래프 중에서 그 가중치의 합이 최소인 트리
# 뭔말임
# 크루스칼

def find_parent(parent, a):
    if parent[a] != a:
        parent[a] = find_parent(parent, parent[a]) # 부모를 타고타고 찾아떠나기
    return parent[a]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

# 정점 개수 V, 간선 개수 E
V, E = map(int, input().split())
# A번 정점부터 B번 정점까지 C만큼 걸린다 (C는 음수일 수도 있고 절댓값이 1,000,000 넘지 않음)
parent = [0] * (V + 1)

for i in range(1, V + 1):
    parent[i] = i

arr = []
result = 0

for _ in range(E):
    A, B, C = map(int, input().split())
    # 단방향이어도 되나?
    # arr[A].append((B, C)) # 부모 인덱스에 (자식 노드, 가중치)
    arr.append((A, B, C))

# 루트 노드 없어도 되나?
# 다익스트라가 음수도 되나? 벨만-포드 or 플로이드 워셜 근데 크루스칼을 써버린 건에 관하여,,
arr.sort(key = lambda x: x[2])

for a, b, c in arr:
    # 서로다르다면 사이클이 아니라는 뜻
    if find_parent(parent, a) != find_parent(parent, b):
        # 묶어주고
        union_parent(parent, a, b)
        # 가중치 더하기
        result += c

print(result)