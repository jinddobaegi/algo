# 빗물
# i를 기준으로 양쪽으로 나보다 높은 놈이 있나요?

H, W = map(int, input().split())
height = list(map(int, input().split()))
ans = 0

for i in range(1, W - 1):
    left = max(height[:i]) # 왼쪽에서 제일 큰 애
    right = max(height[i + 1:]) # 오른쪽에서 제일 큰 애

    temp = min(left, right) # 제일 큰 애중 작은 애만큼이 내가 고일 수 있는 물 양

    if temp > height[i]: # 걔가 나보다 높은 애면
        ans += temp - height[i] # 고일 수 있는 물 양만큼 정답에 더해주기

print(ans)