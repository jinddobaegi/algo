from collections import deque

K = int(input())

for tc in range(K):
    ans = 'YES'
    V, E = map(int, input().split())
    node_lst = [[] * (V + 1) for _ in range(V + 1)]
    for i in range(E):
        u, v = map(int, input().split())
        node_lst[u].append(v) # 양방향으로 하면 까다로우니까
    # print(f'{tc} {node_lst}')
    visited1 = [] # 번갈아가면서
    visited2 = [] # 하나씩 넣어줘
    q = deque()

    # while 돌 때 마다 cnt 하나씩 증가시키면서
    # 그걸 2로 나누는 방법으로 번갈아서 visited1과 visited2에 해당 노드를 추가함
    # 단방향으로 노드리스트에 연결된 노드들 넣어주고
    # 꼬리 잡기로 따라가면서 번갈아 vst1, vst2에 넣어주는데
    # 이미 해당 리스트 안에 넣어져 있으면
    # 답을 No로 바꿔서 출력하기.
    def bfs(v, visited1, visited2):
        global ans
        q.append(v)
        cnt = 0
        while q:
            i = q.popleft()
            if (node_lst[i] not in visited2) and cnt // 2:
                visited1.append(node_lst[i])
                q.append(node_lst[i])
                cnt += 1
            elif (node_lst[i] not in visited1) and not cnt // 2:
                visited2.append(node_lst[i])
                q.append(node_lst[i])
                cnt += 1
            else:
                ans = 'No'

    bfs(1, visited1, visited2)
    print(ans)

"""
TypeError: list indices must be integers or slices, not list
"""