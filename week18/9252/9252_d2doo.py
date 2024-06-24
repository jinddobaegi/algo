# LCS2
# 최장 공통 수열 머시꺵이

first = [0] + list(map(str, input()))
second = [0] + list(map(str, input()))

l_first = len(first)
l_second = len(second)
# arr = [[0] * l_second for _ in range(l_first)] # 정수형은 길이를 잴 수 없다
arr = [[""] * l_second for _ in range(l_first)]

for i in range(1, l_first):
    for j in range(1, l_second):
        if first[i] == second[j]:
            arr[i][j] = arr[i - 1][j - 1] + first[i]
        else: # 큰 숫자 넣어주기!
            if len(arr[i - 1][j]) > len(arr[i][j - 1]):
                arr[i][j] = arr[i - 1][j]
            else:
                arr[i][j] = arr[i][j - 1]

ans = arr[-1][-1] # 제일 끝

if len(ans) > 0:
    print(len(ans))
    print(ans)
else:
    print(0)