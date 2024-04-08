# 트리의 지름
# 골드 4

# 문제


# 전략
# dfs 두번 돌리기
# 양방향 연결 리스트로 저장
# 결국 시작과 끝점까지 가는동안의 가중치의 합이 가장 큰 값을 출력하면 됨


import sys
sys.stdin = open("input.txt")
sys.setrecursionlimit(10 ** 5)  # 재귀 깊이 설정

# 입력
n = int(sys.stdin.readline())
tree = [[] for _ in range(n+1)]

for _ in range(n-1):
    parent, baby, weight = map(int, sys.stdin.readline().split())
    # 부모 노드 값에 해당하는 자식과 가중치
    tree[parent].append((baby, weight))
    # 자식 노드 값에 해당하는 부모와 가중치
    tree[baby].append((parent, weight))
# print(tree)

def dfs(start, distance): # 시작 노드 , 가중치
    # 반복문 돌면서 현재 노드 & 연결 노드, 연결노드 가중치 확인
    for parent, baby in tree[start]:
        if visited[parent] == -1:  # 아직 방문을 안 한것도 탐색
            visited[parent] = distance + baby
            dfs(parent, distance + baby)
    return

visited = [-1] * (n+1)  # 전부 -1로 놓는 이유가 뭘까...?
visited[1] = 0  # 시작노드는 가중치 초기화
dfs(1, 0)

# .첫 노드에서 가장 먼 노드 찾긔
far = visited.index(max(visited))

visited = [-1] * (n+1)
visited[far] = 0  # 먼 노드 가중치 고히ㅘ
dfs(far, 0)

print(max(visited))
