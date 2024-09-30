# 작업
# 위상정렬

from collections import deque

N = int(input())
works = [list(map(int, input().split())) for _ in range(N)]
q = deque()
indegree = [0] * (N + 1)  # 진입차수
cost = [0] * (N + 1)  # 각 작업을 완료하는 데 걸리는 총 시간
todo = [[] for _ in range(N + 1)]  # 선행 작업 정보

# 초기화
for i in range(1, N + 1):
    work = works[i - 1] # for문 안돌리기 위해
    cost[i] = work[0]  # 해당 작업의 소요 시간
    if work[1] != 0:
        for j in work[2:]:
            todo[j].append(i)  # j 작업이 완료되어야 i 작업을 시작할 수 있음
        indegree[i] = work[1]  # 진입차수 저장

# 진입차수가 0인 작업을 큐에 추가
for i in range(1, N + 1):
    if indegree[i] == 0:
        q.append(i)

# 위상 정렬 수행
while q:
    now = q.popleft() # 해당 작업(now)을 끝내면 now가 선행되어야 할 수 있던 작업을 할 수 있음.

    for next_work in todo[now]: # todo에 저장해 둔 후발대(?)를 꺼내며 작업 시작
        indegree[next_work] -= 1  # 진입차수 감소
        # 다음 작업의 총 소요 시간 업데이트 (현재 작업을 완료하고 다음 작업 시작)
        cost[next_work] = max(cost[next_work], cost[now] + works[next_work - 1][0]) # 병렬적으로 작업 가능하기 때문에 제일 오래 걸리는 친구로 업데이트

        # 진입차수가 0이 되면 큐에 추가
        if indegree[next_work] == 0:
            q.append(next_work)

# 모든 작업을 완료하는 데 걸리는 최소 시간 출력
print(max(cost))
