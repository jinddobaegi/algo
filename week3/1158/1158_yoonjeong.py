N, K = map(int, input().split())
arr = []
ans = []

for i in range(1, N+1):
    arr.append(i)

idx = 0
for i in range(N):
    idx += K - 1
    if idx >= len(arr):
        idx %= len(arr)

    ans.append(arr.pop(idx))

print('<' + ', '.join(map(str, ans)) + '>')