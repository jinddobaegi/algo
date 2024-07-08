import sys
sys.stdin = open("week16/1325/1325.txt")
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

#A가 B를 신뢰하면 B를 해킹하면 A를 자동해킹한다. 한번에 가장많은 컴퓨터를 해킹할 . 수있는 컴퓨터의 번호를 오름 차순으로 출력한다. 
#1이랑 2랑 같으면 1, 2로 출력 하나이면 하나만 출력
#첫 줄에 N개의 컴퓨터, M개의 줄에 신회하는 관계가 A B의 형식으로 들어온다.
#음 내생각에는 트리를 만들고 가장 상단의 루트를 구하면 될듯하다.


n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[b].append(a)

def dfs(start):
    stack = [start]
    visited = [False] * (n + 1)
    visited[start] = True
    cnt = 1
    while stack:
        node = stack.pop()
        for neighbor in graph[node]:
            if not visited[neighbor]:
                visited[neighbor] = True
                stack.append(neighbor)
                cnt += 1
    return cnt

result = []
max_value = -1
for i in range(1, n + 1):
    if graph[i]:
        value = dfs(i)
        if value > max_value:
            result = [i]
            max_value = value
        elif value == max_value:
            result.append(i)

print(*sorted(result))