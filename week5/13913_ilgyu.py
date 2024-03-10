import sys
sys.stdin = open('input.txt')
from collections import deque

N, K = map(int, input().split()) # N = 수빈이 위치, K = 동생 위치
visited = [False] * 100001 # 방문 여부 체크
prev = [-1] * 100001 # 이전 위치를 기록

# q에 경로를 str형식으로 담으니까 시간초과? runtime에러남
def find_path(start, end):
    q = deque([start])
    visited[start] = True

    while q:
        current = q.popleft()
        if current == end:
            break

        for next in (current - 1, current + 1, current * 2):
            if 0 <= next < 100001 and not visited[next]:
                visited[next] = True
                q.append(next)
                prev[next] = current # 현재 위치에서 next 위치로 이동함을 기록

    # 경로 재구성
    # 생각 못해낸 부분
    path = []
    while end != -1:
        path.append(end)
        end = prev[end]
    path.reverse() # 시작 위치부터 재구성하기 위해 순서를 뒤집음

    return path


# 초기에 end는 목표 위치 K인 17입니다.
# path 배열에 end를 추가하고, end를 prev[end]로 업데이트합니다. 이를 end가 시작 위치 N으로 업데이트될 때까지 (즉, end가 -1이 될 때까지, -1은 시작 위치로 돌아갔음을 의미) 반복합니다.
# 예시로, 만약 prev[17] = 16, prev[16] = 8, prev[8] = 4, prev[4] = 5라고 가정해보겠습니다. 이 경우, 역추적을 시작하면 17에서 시작하여 5로 끝나는 경로를 찾을 수 있습니다: 17 -> 16 -> 8 -> 4 -> 5.
# 하지만, 우리가 원하는 경로는 시작 위치에서 목표 위치로 가는 순서이므로, 마지막에 경로를 뒤집어 줍니다(path.reverse()). 결과적으로 경로는 5 -> 4 -> 8 -> 16 -> 17이 됩니다.

# 함수 실행 및 결과 출력
path = find_path(N, K)
print(len(path)-1) # 경로의 길이는 위치의 수 - 1
print(" ".join(map(str, path))) # 경로 출력