import sys
sys.stdin = open('input.txt')

# 실패
# n, k = map(int, input().split())
#
# x_place = [0] * (3000001)
# for _ in range(n):
#     g, x = map(int, input().split())
#     x_place[x] = g
#
# # print(x_place[7])
# ans = 0
# for i in range(k, 3000001-k):
#     semi_ans = 0
#     for j in range(i-k, i+k+1):
#         if x_place[j] != 0:
#             semi_ans += x_place[j]
#             # print(semi_ans)
#     # print(semi_ans)
#     ans = max(ans, semi_ans)
# print(ans)

# 슬라이딩 윈도우
n, k = map(int, input().split())
numbers = [0] * 1000001
end = 0
for _ in range(n):
    g, x = map(int, input().split())
    numbers[x] = g
    end = max(end, x) # 아래 for문 돌릴 때 불필요한 연산 안하려고 end값을 여기서 정해놓음

step = 2 * k + 1 # 양쪽으로 k만큼 팔을 벌릴 수 있고 기준점까지 확인해야하니까 ( 검사하는 범위라고 생각하면 됨)
window = sum(numbers[:step]) # 검사한 범위에 있는 숫자들의 합
ans = window
# print(window)
for i in range(step, end+1):
    # 뒤에 더해주고 앞에 빼기
    window += numbers[i] # 뒤
    window -= numbers[i-step] # 뒤에서 하나 더해줬으니까 앞에서 하나 뺴줌
    ans = max(ans, window)
print(ans)
# k에다가 3 넣고 생각해보면 댐
