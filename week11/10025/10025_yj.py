import sys
input = sys.stdin.readline

N, K = map(int, input().split())  # 얼음 양동이 개수, 움직일 수 있는 범위
arr = [0] * 1000001

for _ in range(N):
    g, x = map(int, input().split())  # 얼음의 양, 양동이의 좌표
    arr[x] = g

s = 0
e = 2 * K
temp_sum = sum(arr[s:e+1])
max_sum = temp_sum

# 끝점이 1000000을 넘지 않을 때까지 s, e 갱신해서 계산
while e < 1000000:
    temp_sum -= arr[s]
    s += 1
    e += 1
    temp_sum += arr[e]
    max_sum = max(temp_sum, max_sum)

print(max_sum)
