import sys
sys.stdin = open("week27/14226/14226.txt")
input = sys.stdin.readline
from collections import deque

S = int(input())

def cal():
    queue = deque([(1, 0, 0)])  # 초기 상태 화면 이모티콘 수, 클립보드 이모티콘 수, 동작 횟수
    visited = set((1, 0))  # 방문한 상태를 기록하기 위한 집합

    while queue:
        emo, clip, count = queue.popleft()

        if emo == S:
            return count

        # 1. 복사 
        if (emo, emo) not in visited:
            visited.add((emo, emo))
            queue.append((emo, emo, count + 1))

        # 2. 붙여넣기 
        if clip > 0 and (emo + clip, clip) not in visited:
            visited.add((emo + clip, clip))
            queue.append((emo + clip, clip, count + 1))

        # 3. 삭제 
        if emo > 1 and (emo - 1, clip) not in visited:
            visited.add((emo - 1, clip))
            queue.append((emo - 1, clip, count + 1))

result = cal()
print(result)