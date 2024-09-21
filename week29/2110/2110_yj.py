N, C = map(int, input().split())
arr = [int(input()) for _ in range(N)]
arr.sort()

s = 1
e = arr[-1] - arr[0]
ans = 0

def binary(arr, s, e):
    while s <= e:
        global ans
        m = (s+e) // 2
        current = arr[0]
        cnt = 1

        for i in range(1, N):
            if arr[i] >= current + m:
                cnt += 1
                current = arr[i]

        if cnt >= C:
            s = m + 1
            ans = m
        else:
            e = m - 1

binary(arr, s, e)
print(ans)