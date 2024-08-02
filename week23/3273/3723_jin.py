from sys import stdin

input = stdin.readline
N = int(input())
seq = list(map(int, input().split()))  # 중복 x
x = int(input())

seq.sort()

# 두 수를 골랐을 때
# 합이 x가 되는 (ai, aj) 쌍의 수
# 쌍이라고 한다는 건, 순서는 상관 없는 듯

# 양 끝에서 와보자
# 왼쪽 오른쪽 끝에서부터 출발
# 둘 합이 x보다 작으면 -> 왼쪽 거 오른쪽으로
# x보다 크면 -> 오른쪽 거 왼쪽으로

p1 = 0
p2 = N-1
cnt = 0
while p1 < p2:
    tmp = seq[p1] + seq[p2]
    if tmp == x:
        cnt += 1
        p1 += 1
        p2 -= 1
    elif tmp < x:
        p1 += 1
    else:
        p2 -= 1

print(cnt)

# 시간 초과
# visited = [0] * N
# for i in range(1, N):   # i: 1 ~ N-1
#     if seq[i] >= x:
#         continue
#     for j in range(i):  # j: 0 ~ i-1
#         if visited[j]:
#             continue
#         if seq[i] + seq[j] == x:
#             visited[i] = 1
#             visited[j] = 1
#             cnt += 1