# 피보나치 수열
# 첫째 둘째 항이 1이며 그 뒤로 바로 앞 두 항의 합인 수열
N = 7


# 1. 기본 재귀
def fibo(n):
    if n < 3:
        return 1
    else:
        return fibo(n - 1) + fibo(n - 2)


print(fibo(N))


# 2. DP - recursive
memo = [0] * (N+1)
memo[1] = 1
memo[2] = 1


def fibo_dp_rec(n):
    if n < 3:
        return memo[n]
    else:
        if memo[n] == 0:  # 이게 없어도 작동은 하는데, 효율적이지 못함
            memo[n] = fibo_dp_rec(n-1) + fibo_dp_rec(n-2)
        return memo[n]


print(fibo_dp_rec(N))


# 3. DP - iterative
# 내부 테이블을 생성하여
# for 문을 도는 것이 핵심!
def fibo_dp_iter(n):
    f = [0] * (n+1)
    f[1] = f[2] = 1
    for i in range(3, n+1):
        f[i] = f[i-1] + f[i-2]
    return f[n]


print(fibo_dp_iter(N))