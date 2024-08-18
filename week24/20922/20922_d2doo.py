# 겹치는 건 싫어

N, K = map(int, input().split())
arr = list(map(int, input().split()))
start, end = 0, 0
cnt = [0] * (max(arr) + 1) # N이 아님
ans = 0

while end < N:
    if cnt[arr[end]] < K: # 허용범위를 넘지 않으면
        cnt[arr[end]] += 1 # 추가해주고 한 칸 앞으로 가기
        end += 1
    else:
        cnt[arr[start]] -= 1
        start += 1
    answer = max(answer, end - start)
print(ans)