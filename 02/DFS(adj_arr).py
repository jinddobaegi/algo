'''
7 8
V E
정점의 개수 7
간선의 개수 8
그래프 모양은 아래처럼 주어질 것임
1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7
이어진 노드들을 두 개씩 묶어서 표현한 것
v1 w1 v2 w2 ...
두 개가 하나의 '엣지'임

7 8
1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7

'''

# 시작 정점, 노드 개수, 인접행렬
def dfs(n, V, adj_arr):
    stack = []
    visited = [0] * (V+1)
    visited[n] = 1  # 방문 표시
    print(n)  # 그때마다 처리할 동작 -> print()

    while True:
        for w in range(1, V+1):
            # 인접 + 미방문 찾자
            if adj_arr[n][w]==1 and visited[w]==0:
                # 그럼 방문하고, 처리 동작 수행
                stack.append(w)
                visited[w] = 1
                print(w)
                n = w
                break
        # for-else: for문을 정상적으로 다 돌면 수행
        # 즉 n과 인접한 정점 중 방문하지 않은 곳이 없는 경우, else로 넘어옴
        else:
            # 마지막 갈림길로 돌아가기 위함
            if stack:
                n = stack.pop()
            # 이전 갈림길을 모두 가봤으면
            else:
                break

    return

V, E = map(int, input().split())
arr = list(map(int, input().split()))
adj_arr = list([0]*(V+1) for _ in range(V+1))

for i in range(E):
    v1, v2 = arr[i*2], arr[i*2+1]
    adj_arr[v1][v2] = 1
    adj_arr[v2][v1] = 1


dfs(1, V, adj_arr)