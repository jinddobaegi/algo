import sys
sys.stdin = open("week13/1725/1725.txt")
input = sys.stdin.readline

# 시간초과
row = int(input())
graph = []
for _ in range(row):
    graph.append(int(input()))
result = []
for i in range(row):
    left, right = i, i
    while left > 0 and graph[left-1] >= graph[i]:
        left -= 1
    while right < row-1 and graph[right+1] >= graph[i]:
        right += 1
    result.append((right-left+1)*graph[i])
print(max(result))
        

        
#다시
import sys
sys.stdin = open("week13/1725/1725.txt")
input = sys.stdin.readline

row = int(input())
graph = []
for _ in range(row):
    graph.append(int(input()))
graph.append(0)

stack = [] #0, 1, 2, 3, 4, 5, 6, 7, 8, 9 ~
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
    