arr = list(range(1,50,2))


def bin_search(arr, start, end, target):
    while start <= end:
        mid = (start + end) // 2
        if arr[mid] == target:
            return 1
        # target이 중앙값보다 큰 경우
        elif arr[mid] < target:
            start = mid + 1
        # target이 중앙값보다 작은 경우
        else:
            end = mid - 1
    return -1


res = bin_search(arr, 0, len(arr)-1, 10)
print(res)