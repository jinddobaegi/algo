arr = [
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12],
    [13,14,15,16],
    [17,18,19,20]
]

N = len(arr)
M = len(arr[0])

# 행(i)는 쭉 감
# 열(j)은 짝수행일 때 오른쪽으로, 홀수행일 때 왼쪽으로

for i in range(N):
    for j in range(M):
        # 홀수 행일 때, M-1-j가 되면 된다
        print(arr[i][j + (M - 1 - 2 * j) * (i % 2)], end=' ')