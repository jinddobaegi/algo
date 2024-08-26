import sys
sys.stdin = open("week26/16940/16940.txt")
input = sys.stdin.readline
from collections import deque

# def bfs(graph, v):
#     visited = [False] * len(graph)
#     visited[v] = True
#     queue = deque([v])
#     linelist = [] 
#     # print(linelist)ㄷ
#         node = queue.popleft()
#         linelist.append(node)

#         for neighbor in graph[node]:
#             if not visited[neighbor]:
#                 visited[neighbor] = True
#                 queue.append(neighbor)
#     return linelist


# N = int(input())
# graph = [[] for _ in range(N+1)]
# for _ in range(N-1):
#     a, b = map(int, input().split())
#     graph[a].append(b)
#     graph[b].append(a)
# bfs_result = list(map(int, input().split()))

# linelist = bfs(graph, 1)
# # print(linelist)

# if linelist == bfs_result:
#     print(1)
# else:
#     print(0)

from collections import deque
import sys
input = sys.stdin.readline

def bfs_check(graph, bfs_order):
    N = len(graph) - 1
    visited = [-1] * (N + 1)
    children = [set() for _ in range(N + 1)]
    
    # BFS 탐색 수행
    queue = deque([1])
    visited[1] = 0
    index = 1  # bfs_order에서 탐색 순서
    
    while queue:
        current = queue.popleft()
        
        child_set = set()  # 현재 노드의 자식 노드 집합
        
        # 인접한 노드들 탐색
        for neighbor in graph[current]:
            if visited[neighbor] == -1:
                visited[neighbor] = visited[current] + 1
                queue.append(neighbor)
                child_set.add(neighbor)
        
        # 주어진 BFS 순서에서 자식 노드들이 올바르게 배치되었는지 확인
        expected_child_set = set(bfs_order[index:index + len(child_set)])
        if child_set != expected_child_set:
            return False
        
        # 다음 자식 노드들을 확인하도록 index를 증가
        index += len(child_set)
    
    return True

def solve():
    N = int(input())
    graph = [[] for _ in range(N + 1)]
    
    for _ in range(N - 1):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)
    
    bfs_order = list(map(int, input().split()))
    
    # BFS 순서의 첫 번째 노드가 1인지 확인 (1번 노드부터 시작해야 함)
    if bfs_order[0] != 1:
        print(0)
        return
    
    # BFS 순서가 올바른지 확인
    if bfs_check(graph, bfs_order):
        print(1)
    else:
        print(0)

solve()