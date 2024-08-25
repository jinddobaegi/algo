# BFS 스페셜 저지
from collections import deque, defaultdict

def bfs(): # 같은 레벨의 노드들끼리 묶어주는 작업
    q = deque()
    q.append(1)
    visited[1] = 1

    while q:
        x = q.popleft()
        for y in tree[x]:
            if visited[y] == 1:
                continue
            visited[y] = 1
            level[x].append(y)
            q.append(y)

N = int(input())
tree = [[] for _ in range(N + 1)]
for _ in range(N - 1):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)

request = list(map(int, input().split()))
visited = [0] * (N + 1)
level = defaultdict(list) # 없는 키값을 불러오면 자동으로 []로 초기화해서 불러와 줌.

if request[0] != 1:
    print(0)
else:
    bfs()

    q = deque()
    q.append(1)
    idx = 1 # 시작 노드 1개

    while q:
        now = q.popleft()
        children = level[now] # 현재 레벨의 노드들 꺼내기
        length = len(children)
        next_nodes = request[idx:idx+length]

        if set(children) != set(next_nodes):
            print(0)
            break

        q.extend(next_nodes)
        idx += length
    else: print(1) # else를 왜 꼭 붙여야할까나

