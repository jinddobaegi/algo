# 최소 스패닝 트리
N = int(input())  # 컴퓨터의 수
M = int(input())  # 연결할 수 있는 선의 수
edges = []
for _ in range(M):
    a, b, c = map(int, input().split())
    edges.append([a, b, c])

edges.sort(key=lambda x: x[2])  # 비용 기준으로 정렬
parents = [i for i in range(N+1)]

def find_set(x):
    if parents[x] == x:
        return x

    parents[x] = find_set(parents[x])
    return parents[x]

def union(x, y):
    x = find_set(x)
    y = find_set(y)

    if x == y:
        return

    if x < y:
        parents[y] = x
    else:
        parents[x] = y

cnt = 0
sum_cost = 0
for a, b, c in edges:
    if find_set(a) != find_set(b):
        cnt += 1
        sum_cost += c
        union(a, b)
        if cnt == N:
            break

print(sum_cost)