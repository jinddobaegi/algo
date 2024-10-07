# 행복 유치원
N, K = map(int, input().split())
children = list(map(int, input().split()))
height = []
for i in range(1, N):
    height.append(children[i] - children[i - 1])

height.sort()
print(sum(height[:N-K]))
