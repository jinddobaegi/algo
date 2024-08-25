# 소트
# 뭔 알고리즘임 이거?

N = int(input())
arr = list(map(int, input().split()))
S = int(input())
i = 0

while S > 0 and i < N:
    idx = arr.index(max(arr[i:i+S+1])) # 제일 큰 수 인덱스
    if idx > 0 and idx != i:
        arr[idx], arr[idx-1] = arr[idx-1], arr[idx]
        S -= 1
    else:
        i += 1
print(*arr)