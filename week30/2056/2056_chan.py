import sys
sys.stdin = open("week30/2056/2056.txt")

from collections import deque

def solution():
    # 입력 받기
    N = int(input())  # 작업의 개수
    time = [0] * (N + 1)  # 각 작업에 걸리는 시간을 저장할 리스트
    indegree = [0] * (N + 1)  # 진입 차수 리스트
    graph = [[] for _ in range(N + 1)]  # 그래프 리스트

    # 각 작업에 대한 정보 입력 받기
    for i in range(1, N + 1):
        data = list(map(int, input().split()))  # 입력받은 데이터를 리스트로 저장
        time[i] = data[0]  # 첫 번째 값은 작업에 걸리는 시간
        num_predecessors = data[1]  # 두 번째 값은 선행 작업의 수
        for j in range(2, 2 + num_predecessors):  # 선행 작업 번호들
            predecessor = data[j]
            graph[predecessor].append(i)  # 선행 작업의 관계를 그래프에 저장
            indegree[i] += 1  # 현재 작업의 진입 차수 증가

    # 위상 정렬을 위한 큐
    queue = deque()
    result = [0] * (N + 1)  # 결과 시간 리스트 (최소 작업 완료 시간을 저장)

    # 진입 차수가 0인 작업을 큐에 삽입
    for i in range(1, N + 1):
        if indegree[i] == 0:
            queue.append(i)
            result[i] = time[i]  # 해당 작업의 완료 시간을 바로 저장

    # 위상 정렬 수행
    while queue:
        current = queue.popleft()

        # 현재 작업에서 이어지는 작업들을 확인
        for next_task in graph[current]:
            indegree[next_task] -= 1  # 진입 차수를 1 감소
            result[next_task] = max(result[next_task], result[current] + time[next_task])

            # 진입 차수가 0이 되면 큐에 삽입
            if indegree[next_task] == 0:
                queue.append(next_task)

    # 결과 출력: 모든 작업을 완료하는 데 걸리는 최소 시간
    print(max(result))

# 함수 실행
solution()
