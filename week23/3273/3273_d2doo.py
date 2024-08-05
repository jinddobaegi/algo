# 두 수의 합
# 투 포인터~~~~~

N = int(input())
nums = list(map(int, input().split()))
x = int(input())
ans = 0

nums.sort()

one, two = 0, N - 1 # 양 끝에서 출발
while one < two:
    sum_num = nums[one] + nums[two]
    if sum_num == x:
        ans += 1
        one += 1
        two -= 1
    elif sum_num < x:
        one += 1
    elif sum_num > x:
        two -= 1

print(ans)
