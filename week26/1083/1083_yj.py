# S번 이내로 교환하는 동안 사전순으로 가장 뒷서는 배열 출력
N = int(input())
arr = list(map(int, input().split()))
S = int(input())

for i in range(N):
    # 큰 수가 최대한 앞쪽으로 오도록 만들어야 한다
    # 현재 위치에서 S만큼 떨어진 거리 내에서 최댓값 찾기
    max_n = arr.index(max(arr[i: min(N, i+S+1)]))

    # max_n을 앞쪽으로 이동시키기
    for j in range(max_n, i, -1):
        arr[j], arr[j-1] = arr[j-1], arr[j]

    S -= (max_n - i)
    if S == 0:
        break

print(*arr)