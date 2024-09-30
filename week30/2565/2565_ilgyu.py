import sys
sys.stdin = open('input.txt')

n = int(input())
graph = []

for _ in range(n):
    a, b = map(int, input().split())
    graph.append([a, b])

# 1. 전깃줄이 교차하지 않는다를 판단하는 기준
# 2. 교차하지 않는 방법이 여러가지일 수 있음 => 완탐?
graph.sort()
line = []
for a, b in graph:
    line.append(b)

# print(line)

# line에서 오름차순을 만드는데 가장 긴 오름차순
dp = [1] * n
for i in range(1, n):
    for j in range(i):
        if line[j] < line[i]:
            dp[i] = max(dp[i], dp[j] + 1)

print(n - max(dp))