# SelectionSort
# 전체에서 가장 작은 데이터 선택, 맨 앞과 교환
# 그 다음 작은 데이터 선택, 그 다음과 교환
# 반복

arr_1 = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

N = len(arr_1)

# 시작 지점을 위한 for문
for i in range(N-1):
    min_v = 99
    idx = -1
    for j in range(i, N):
        if min_v > arr_1[j]:
            min_v = arr_1[j]
            idx = j
    # min_v가 갱신됨
    arr_1[i], arr_1[idx] = min_v, arr_1[i]

# print(arr_1)

# 재귀를 활용한 선택정렬

arr_2 = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

s = 0
idx2 = -1


def my_func(arr):
    global s
    global idx2

    if s == N:
        return

    min_v = 99
    for k in range(s, N):
        if min_v > arr_2[k]:
            min_v = arr_2[k]
            idx2 = k
    arr_2[s], arr_2[idx2] = arr_2[idx2], arr_2[s]
    s += 1
    my_func(arr_2)


my_func(arr_2)
print(arr_2)

