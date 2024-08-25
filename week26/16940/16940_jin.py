from sys import stdin

input = stdin.readline

N = int(input())
adj_list = list([] for _ in range(N+1))
for _ in range(N-1):
    a, b = map(int, input().split())
    adj_list[a].append(b)
    adj_list[b].append(a)

route = list(map(int, input().split()))

# 어차피 bfs는
# 같은 깊이에 있는 것들을 다 돌고 난 뒤
# 그 다음 깊이의 노드를 돌 수 있다

# 첫 노드(시작점)를 하나 뽑음
# 거기서 갈 수 있는 곳 묶어서 enqueue, 방문표시
# 다음 목적지는 그 묶음 안에 있어야 함
# 그 노드를 찾았다? 그럼 그 묶음 안에서 해당 노드만 제거하고
# 해당 노드에서 이동 가능한 노드들 묶어서 enqueue
# 반복

q = list([] for _ in range(N+1))  # 단계 별로 저장할 것임
visited = [0] * (N+1)
q[1].append(1)
visited[1] = 1
selected = [0] * (N+1)
depth = 1
idx = 0
while depth != N:
    if not q[depth]:
        depth += 1
        continue
    x = route[idx]
    # print(f'd는 {depth}, x는 {x}')
    v = 0
    if x in q[depth]:
        v = x
        q[depth].remove(v)
        selected[v] = 1
        idx += 1
    else:
        break

    for w in adj_list[v]:
        if not visited[w]:
            q[depth+1].append(w)
            visited[w] = 1

if sum(selected) == N:
    print(1)
else:
    print(0)