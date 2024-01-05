# 2^k을 for문과 재귀로 구현
k = 10
num = 2
# 1) for문

res1 = 1
for i in range(k):
    res1 *= 2

# print(res1)


# 2) 재귀

res2 = 1


def my_square(res, num, k, i):
    if k == 0:
        return 1
    elif i == k:
        return res
    else:
        return my_square(res*num, num, k, i+1)


ans = my_square(1, num, k, 0)
print(ans)