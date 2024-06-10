# 효율적인 해킹
# 실버1

'''
컴퓨터 n개
해킹 일타 N피 하려고 함
컴터가 서로 신뢰하는 ㄱ경우 -> 둘다 해킹 가능
최대 해킹할 수 있는 컴퓨터 번호 출력
'''



import sys
input = sys.stdin.readline

from collections import deque

# pypy로 하면 되긴하는데 python3로 하면 시간 초과 나버림...
def bfs(s):
    cnt = 0
    q = deque()
    q.append(s)
    visited[s] = 1

    while q:
        now = q.popleft()
        # 연결된 노드 확인
        for i in graph[now]:
            if visited[i] == 0:
                visited[i] = 1  # 방문처리
                # 큐에다 넣어줘
                q.append(i)
                cnt += 1
    return cnt


n, m = map(int, input().split())

graph = [0 for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    # 반대 방향으로 간선 연결해줘야 신뢰 관계가 연결이 되니까
    graph[b].append(a)

max_cnt = 0
result = []



# 노드 탐색하면서
for i in range(1, n + 1):
    visited = [0] * (n + 1)  # 방문 쳌

    # 탐색 가능한 노드 수
    cnt = bfs(i)
    max_cnt = max(max_cnt, cnt)
    # 노드 번호 별로 카운트 값 저장해주기
    result.append((i, cnt))


for i in result:
    # 최댓값이면
    if i[1] == max_cnt:
        # 노드 번호 출력
        print(i[0], end=' ')