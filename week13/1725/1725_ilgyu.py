import sys
sys.stdin = open('input.txt')

n = int(input())
graph = []
result = 0
cursor = 0 # 현재 x좌표 값
a = 0
for _ in range(n):
    graph.append(int(input()))
print(graph)
graph.append(0) # 히스토그램의 모든 막대를 처리한 후에 스택에 남아 있는 막대들을 쉽게 처리하기 위해서

print(graph)
stack = [(0, graph[0])] # (x좌표, 높이) 저장하는 스택
for i in range(1, n + 1):
    cursor = i
    while stack and stack[-1][1] > graph[i]:
        cursor, temp = stack.pop()
        result = max(result, temp * (i - cursor))
    stack.append((cursor, graph[i]))
# 이해안됨 송찬의 ㅅ ㅂ

print(result)

