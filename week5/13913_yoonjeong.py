# 어떻게 풀어야할지 알 것 같다가도 모르겠음
# 그냥 모르겠다는 소리임
# 검색해서 참고함 ㅠㅠ

from collections import deque

N, K = map(int, input().split())
time = [0] * 100001 # 걸린 시간
path = [0] * 100001 # 루트 기록 (부모 노드를 알기 위해)

q = deque()
q.append(N)

while q:
    x = q.popleft()
    d = [x-1, x+1, 2*x]

    if x == K:
        ans = []
        temp = x  # 역으로 경로를 찾기 위함
        print(time[K]) # 최단시간
        for _ in range(time[K] + 1):
            ans.append(temp)
            temp = path[temp] # 그 전 경로 추가
        print(*ans[::-1])
        break
    for nx in d:
        if 0 <= nx <= 100000 and time[nx] == 0:
            time[nx] = time[x] + 1  # 현재 위치 시간 + 1
            path[nx] = x            # 지나온 위치를 알기 위해 새로운 위치에 이전 위치 정보 넣음
            q.append(nx)