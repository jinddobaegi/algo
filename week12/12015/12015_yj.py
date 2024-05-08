# 가장 긴 증가하는 부분 수열
# 오름차순으로 증가하는 부분 수열 중 가장 길이가 긴 수열
# [10, 20, 10, 30, 20, 50] 인 경우 -> [10, 20, 30, 50]

N = int(input())  # 수열 A의 크기
arr = list(map(int, input().split()))  # 수열
temp = [arr[0]]

def binary(s, e, i):
    while s <= e:
        mid = (s + e) // 2
        if i > temp[mid]:
            s = mid + 1
        else:
            e = mid - 1

    return s

for i in arr:
    if i > temp[-1]:
        temp.append(i)
    else:
        s = 0
        e = len(temp) - 1

        idx = binary(s, e, i)
        temp[idx] = i

print(len(temp))