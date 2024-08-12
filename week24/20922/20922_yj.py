N, K = map(int, input().split())
arr = list(map(int, input().split()))

start = 0
end = 0
ans = 0
cnt = [0] * 100001  # 숫자별 개수 카운트

# 처음부터 하나씩 늘려가면서 계산
while end < N:
    s = arr[start]
    e = arr[end]

    if cnt[e] < K:
        cnt[e] += 1
        end += 1
    else:
        cnt[s] -= 1
        start += 1

    ans = max(end-start, ans)

print(ans)