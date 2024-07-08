# 최소 스패닝 트리
# 주어진 그래프의 모든 정점들을 연결하는 부분 그래프 중에서 그 가중치의 합이 최소인 트리
# 골드4

# 문제
# 첫째 줄에 정점의 개수 V(1 ≤ V ≤ 10,000)와
# 간선의 개수 E(1 ≤ E ≤ 100,000)가 주어진다.
# 다음 E개의 줄에는 각 간선에 대한 정보를 나타내는 세 정수 A, B, C가 주어진다.
# 이는 A번 정점과 B번 정점이 가중치 C인 간선으로 연결되어 있다는 의미
# C는 음수일 수도 있으며, 절댓값이 1,000,000을 넘지 않는다.
# 그래프의 정점은 1번부터 V번까지 번호가 매겨져 있고,
# 임의의 두 정점 사이에 경로가 있다.
# 최소 스패닝 트리의 가중치가 -2,147,483,648보다 크거나 같고,
# 2,147,483,647보다 작거나 같은 데이터만 입력으로 주어진다.

# 전략
# 어게인 유니온 파인드



import sys
input = sys.stdin.readline

V, E = map(int, input().split())
lst = []
for _ in range(E):
    A, B, C = map(int, input().split())
    lst.append((A, B, C)) # 들어오는 족족 일단 담아놓고
# 다담으면 가중치 적은 것부터 오름차순 정렬
lst.sort(key=lambda x: x[2])

# 부모 노드 초기화
parent = [i for i in range(V+1)]

def find(x):
    if parent[x] == x:
        return x
    parent[x] = find(parent[x]) # get_parent 거슬러 올라가면서 parent[x] 값도 갱신
    return parent[x]

def union(x, y):
    x = find(x)
    y = find(y)

    if x < y: # 작은 쪽이 부모가 됨
        parent[y] = x
    else:
        parent[x] = y

# 부모 같은지 판별할라고
def same_parent(x, y):
    return find(x) == find(y)


ans = 0
for a, b, c in lst:
    # 가중치 작은 것부터 추가해가면서 같은 부모인게 아닐 때만 확정시켜
    if not same_parent(a, b):
        union(a, b)
        ans += c

print(ans)
