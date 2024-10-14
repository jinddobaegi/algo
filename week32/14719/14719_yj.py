H, W = map(int, input().split())
block = list(map(int, input().split()))

# 물이 고이는 조건 -> 양쪽에 자신보다 높은 블록이 있어야 한다
# 현재 블록을 기준으로 양쪽에서 가장 높은 블록을 구한 후
# 그 중 낮은 블록과 현재 블록의 차이를 구한다 = 고일 수 있는 물의 양

total = 0
for i in range(1, W-1):  # 맨 왼쪽, 맨 오른쪽은 제외
    left = max(block[:i])  # 현재 위치의 왼쪽에서 가장 높은 블록
    right = max(block[i:])  # 현재 위치의 오른쪽에서 가장 높은 블록

    water = min(left, right) - block[i]
    if water > 0:  # 물이 고일 수 있는 경우
        total += water

print(total)