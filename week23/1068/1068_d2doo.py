# 트리
# DFS 연습~!

def dfs(start):
    arr[start] = -2
    for i in range(N):
        if start == arr[i]: # 순회하는 친구의 부모노드가 나라면(?)
            dfs(i)

N = int(input())
arr = list(map(int, input().split()))
delete = int(input())
cnt = 0

dfs(delete)

for i in range(N):
    if not (i in arr) and arr[i] != -2:
        cnt += 1

print(cnt)