from collections import deque

def bfs(v, visited, node_lst):
    q = deque([v])
    visited[v] = 1
    while q:
        parent = q.popleft()
        for i in node_lst[parent]: # 부모 루트부터 시작하기 때문에, 이미 방문이 되어있다면 부모임. 방문 안되어있으면 자식.
            if not visited[i]:
                visited[i] = 1
                child[i] = parent # q에서 pop한게 부모, 그걸 child list index에 parent 넣어줌.
                q.append(i)

N = int(input())
node_lst = [[] for _ in range(N + 1)]
# print(f'node_list={node_lst}')

visited = [0] * (N + 1)
child = [0] * (N + 1)
for i in range(N-1):
    a, b = map(int, input().split())
    node_lst[a].append(b) # 양방향으로 넣어주기
    node_lst[b].append(a)

bfs(1, visited, node_lst)

for i in range(2, N+1):
    print(child[i])