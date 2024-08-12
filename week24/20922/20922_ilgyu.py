import sys
sys.stdin = open('input.txt')

n, k = map(int, input().split())
arr = list(map(int, input().split()))

counter = [0] * (max(arr) + 1)

start, end = 0, 0
ans = 0
while end < n:
    if counter[arr[end]] < k:
        counter[arr[end]] += 1
        end += 1
    else:
        counter[arr[start]] -= 1 # 해당 start의 숫자는 지나간걸로 표시
        start += 1
    ans = max(end-start, ans)
print(ans)