import sys
sys.stdin = open('input.txt')

n = int(input())
arr = list(map(int, input().split()))
s = int(input())

# 사전순으로 뒷선다 => 최대한 큰 값

for i in range(n):
    max_num = max(arr[i:i+s+1])
    max_idx = arr.index(max_num)

    for j in range(max_idx, i, -1):
        arr[j-1], arr[j] = arr[j], arr[j-1]
        s -= 1

    if s <= 0:
        break
print(*arr)

