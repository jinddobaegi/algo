import sys
sys.stdin = open("week32/14719/14719.txt")

H, W = map(int, input().split())
world = list(map(int, input().split()))

# 오른쪽에서 제일큰수와 왼쪽에서 제일 큰수를 찾고 그 중 작은것을 최대 높이로 설정
# 최대 높이보다 작은 것들만을 물의양 합에 더해 준다.
# 포문으로 움직이기 때문에 다음 웅덩이가 나와도 그부분에서 다시 최대높이를 찾기때문에 가능하다.

def cal():
    sum_value = 0
    
    for i in range(1, W - 1):  
        left_max = max(world[:i])  
        right_max = max(world[i + 1:])  

        water_level = min(left_max, right_max)

        if water_level > world[i]:
            sum_value += water_level - world[i]

    return sum_value

result = cal()
print(result)