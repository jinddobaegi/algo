import sys
sys.stdin = open("week29/2110/2110.txt")
input = sys.stdin.readline

N, C = map(int, input().split())
houses = [int(input()) for _ in range(N)]

houses.sort()

left = 1
right = houses[-1] - houses[0]
result = 0

while left <= right:
    mid = (left + right) // 2     
    now = houses[0]
    count = 1

    for i in range(1, N):
        if houses[i] - now >= mid:
            count += 1
            now = houses[i]
    
    if count >= C:
        result = mid
        left = mid + 1
    
    else:
        right = mid - 1

print(result)

    
