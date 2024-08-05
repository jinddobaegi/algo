N = int(input())
arr = list(map(int, input().split()))
d = int(input())
tree = [[] for _ in range(N)]
cnt = 0

# 트리 구성
for i in range(N):
    if arr[i] == -1:
        r = i
    elif i != d:
        tree[arr[i]].append(i)

# 리프 노드 확인
def dfs(s):
    global cnt

    if not tree[s]:
        cnt += 1
        return

    for c in tree[s]:
        dfs(c)

if d == r:
    print(0)
else:
    dfs(r)
    print(cnt)