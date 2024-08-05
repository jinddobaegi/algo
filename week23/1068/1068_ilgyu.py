import sys
sys.stdin = open('input.txt')

N = int(input())
parents = list(map(int, input().split()))
remove_node = int(input())
# print(parents)
# print(remove_node)

# 트리문제는 일단 트리를 만들어
# 일단 노드를 정보를 만들어
nodes = [i for i in range(N)]
# print(nodes)

def dfs(node):
    parents[node] = -10
    for i in range(N):
        if node == parents[i]: # parents[node]는  node의 부모노드 를 뜻함
            dfs(i)

dfs(remove_node)
cnt = 0
for i in range(N):
    if parents[i] != -10 and i not in parents:
        cnt += 1

print(cnt)


