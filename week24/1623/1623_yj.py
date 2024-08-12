N = int(input())
arr = list(map(int, input().split()))
lst = list(map(int, input().split()))
tree = [[] for _ in range(N+1)]
dp = [[0] for _ in range(N+1)]

# 트리 생성
for i in range(2, N+1):
    tree[lst[i-2]].append(i)