# 부분합
# 투포인터

N, S = map(int, input().split())
arr = list(map(int, input().split()))

start, end = 0, 0
sum_v = arr[0] # 0이면 코드를 다르게 짜야함
length = 1e6

# while sum_v < S: 도 안됨. 커질 때 계산해야 함.
while start < N and end < N:
    if sum_v < S: # 합이 작으면 오른쪽으로 옮겨보고
        end += 1
        if end == N: # 끝에 도달하면 멈춰주고
            break
        sum_v += arr[end] # 합에 end 값을 넣어준다.
    else: # 합이 크다면
        length = min(length, end - start + 1) # 최소값을 저장을 하고
        sum_v -= arr[start] # start 값을 빼주고
        start += 1 # start를 옮긴다.

if length == 1e6:
    print(0)
else:
    print(length)