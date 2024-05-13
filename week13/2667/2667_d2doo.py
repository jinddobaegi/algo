# 단지번호 붙이기
from collections import deque

# 마침 집이 1이라서 visited 안만들어볼게용

def bfs(graph, a, b):
    q = deque()  # 큐 초기화(?)
    q.append((a, b))
    graph[a][b] = 0  # 첫번째 집 a,b를 방문 처리해준다.
    cnt = 1  # 첫번째 집 a,b 를 방문했기 때문에 cnt값을 1로 시작한다.

    while q:
        x, y = q.popleft()
        graph[x][y] = 0
        for i in range(4):  # 델타탐색하면서
            ni = x + di[i]
            nj = y + dj[i]

            # 그래프 넘어가면
            if ni < 0 or ni >= len(graph) or nj < 0 or nj >= len(graph):
                continue

            if graph[ni][nj] == 1:  # 1이면?(방문을 안했고 집임)
                graph[ni][nj] = 0  # 0으로 만들기
                q.append((ni, nj))  # 여기서부터 돌거니까 좌표 추가
                cnt += 1
    return cnt

N = int(input())

graph = []  # 입력받은 그래프
answer = []  # 집 몇개인지

for _ in range(N):
    graph.append(list(map(int, input())))

# 한 점을 기준으로 (위 아래 왼쪽 오른쪽) 으로 한칸 씩 이동할 좌표 설정
di = [0, 0, 1, -1]
dj = [1, -1, 0, 0]

for i in range(N):
    for j in range(N):
        if graph[i][j] == 1:
            cnt = bfs(graph, i, j) #bfs로 cnt 리턴받음
            answer.append(cnt)

answer.sort()  # 정렬

print(len(answer))  # 총 단지수
for ans in answer:  # 각 단지마다 집의 수 오름차순
    print(ans)