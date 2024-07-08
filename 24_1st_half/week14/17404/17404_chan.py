import sys
sys.stdin = open("week14/17404/17404.txt")
input = sys.stdin.readline

# 다이나믹 알고리즘은 앞에서 계산한 값을 저장해두고 다음 계산에 사용한다.

# 1번 집의 색은 2번, N번 집의 색과 같지 않아야 한다. 중요!

# N번 집의 색은 N-1번, 1번 집의 색과 같지 않아야 한다. 중요!
# i(2 ≤ i ≤ N-1)번 집의 색은 i-1, i+1번 집의 색과 같지 않아야 한다.

# 첫번째 집과 마지막 집의 색은 같지 않아야 한다.

# 예제 입력
# 3
# 26 40 83
# 49 60 57
# 13 89 99

# 예제 출력
# 110

#1149와는 조건이 다른다. 따라서 출력값도 다르다.

house = int(input())
cost = [list(map(int, input().split())) for _ in range(house)]
print("cost = " , cost)
result = 1000001

for i in range(3): # 0, 1, 2
    dp = [[1001]*3 for _ in range(house)] # 2차원 배열 생성 
    dp[0][i] = cost[0][i] # 0번째 집의 색깔을 정한다.
    for j in range(1, house):
        dp[j][0] = min(dp[j-1][1], dp[j-1][2]) + cost[j][0]
        dp[j][1] = min(dp[j-1][0], dp[j-1][2]) + cost[j][1]
        dp[j][2] = min(dp[j-1][0], dp[j-1][1]) + cost[j][2]
    dp[-1][i] = 1000001
    result = min(result, min(dp[-1]))
                 
print(result)

                           

