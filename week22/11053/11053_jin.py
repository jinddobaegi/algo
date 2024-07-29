from sys import stdin

input = stdin.readline


def bin_search(s, e, t):
    while s <= e:
        m = (s+e)//2
        # LIS에서 값을 찾아야 하는데
        # arr에서 찾아서 한참 헤맸다;;
        if LIS[m] == t:
            return m
        elif LIS[m] > t:
            e = m - 1
        else:
            s = m + 1

    return s


N = int(input())
arr = list(map(int, input().split()))
LIS = [0]

# 원소를 하나씩 보면서
# 마지막보다 크면 lis에 추가
# 마지막보다 작으면 나보다 작은 수 찾아서 그 다음 인덱스의 값에 넣자

for i in range(N):
    num = arr[i]
    if num > LIS[-1]:
        LIS.append(num)
    else:
        idx = bin_search(0, len(LIS)-1, num)
        LIS[idx] = num

print(len(LIS)-1)