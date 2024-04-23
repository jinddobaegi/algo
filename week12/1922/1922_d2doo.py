# 네트워크 연결
# 각 컴퓨터를 연결하는데 필요한 비용이 주어졌을 때 모든 컴퓨터를 연결하는데 필요한 최소비용을 출력하라.
# 모든 컴퓨터를 연결할 수 없는 경우는 없다.
# MST

def find_parent(a):
    # 찐 노드 찾아가기
    if parent[a] != a:
        parent[a] = find_parent(parent[a])
    return parent[a]

def union_parent(a, b):
    # 각자의 노드를 찾아주고
    a = parent[a]
    b = parent[b]
    # 작은 노드가 부모노드가 됨.
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

N = int(input()) # 컴퓨터 수
M = int(input()) # 선의 수
connection = []

for _ in range(M):
    a, b, c = map(int, input().split())
    connection.append((a, b, c))

# 비용별로
connection.sort(key = lambda x : x[2])

# 부모 초기화
parent = [i for i in range(N + 1)]

cost = 0
for a, b, c in connection:
    if find_parent(a) != find_parent(b):
        union_parent(a, b)
        cost += c

print(cost)
