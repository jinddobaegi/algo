import sys
sys.stdin = open('input.txt')

n, s = map(int, input().split())
arr = list(map(int, input().split()))

start, end = 0, 0
min_length = float('inf')
res = 0

while True:
    if res >= s:
        min_length = min(min_length, end-start)
        res -= arr[start] # 기존에 있던 왼쪽 값 빼주기
        start += 1

    elif end == n:
        break
    else: # 더 작으면 end 늘려주기
        res += arr[end]
        end += 1
if min_length == float('inf'):
    print(0)
else:
    print(min_length)




