N, S = map(int, input().split())
arr = list(map(int, input().split()))

start = 0
end = 0
sum = 0
min_len = int(1e9)

while True:
    if sum >= S:
        min_len = min(end - start, min_len)
        sum -= arr[start]
        start += 1
    else:
        if end == N:
            break
        sum += arr[end]
        end += 1

if min_len == int(1e9):
    print(0)
else:
    print(min_len)