from sys import stdin
from collections import deque

input = stdin.readline

# 교차하는 전깃줄이 없도록
# 제거해야 하는 전깃줄 최소 개수

N = int(input())
arr = list(tuple(map(int, input().split())) for _ in range(N))
arr.sort()
# print(arr)

stack = deque()
cnt = 0
for i in range(N):
    while stack and stack[-1][1] > arr[i][1]:
        stack.pop()
        cnt += 1

    stack.append(arr[i])

print(cnt)