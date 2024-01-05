arr = [
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12],
    [13,14,15,16]
]

N = len(arr)
M = len(arr[0])

for i in range(N):
    for j in range(M):
        if i > j:
            arr[i][j], arr[j][i] = arr[j][i], arr[i][j]

print(arr)