import sys
sys.stdin = open("week14/1725/1725.txt")
input = sys.stdin.readline

row = int(input())
graph = []
for _ in range(row):
    graph.append(int(input()))
graph.append(0)

stack = []
result = 0

for i in range(row+1):
    while stack and graph[stack[-1]] > graph[i]:
        height = graph[stack.pop()]
        width = i
        if stack:
            width -= stack[-1] + 1 
        result = max(result, height * width)
    stack.append(i)
    print("stack",stack)

print(result)

