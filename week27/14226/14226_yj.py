from collections import deque

S = int(input())
visited = [[-1]*1001 for _ in range(1001)]

def bfs():
    q = deque()
    q.append((1, 0))
    visited[1][0] = 0
    while q:
        e, clip = q.popleft()

        # 이모티콘을 S개 만들었을 때
        if e == S:
            print(visited[e][clip])
            break

        # 복사해서 저장
        if visited[e][e] == -1:
            visited[e][e] = visited[e][clip] + 1
            q.append((e, e))

        # 클립보드 붙여넣기
        if e + clip <= S and visited[e+clip][clip] == -1:
            visited[e+clip][clip] = visited[e][clip] + 1
            q.append((e+clip, clip))

        # 하나 삭제
        if e - 1 >= 0 and visited[e-1][clip] == -1:
            visited[e-1][clip] = visited[e][clip] + 1
            q.append((e-1, clip))

bfs()