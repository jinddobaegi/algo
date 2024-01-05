# 팩토리얼은 1부터 N까지의 수를 모두 곱하는 것이다
N = 5


# 1. 기본 재귀
def fact_rec(n):
    if n < 2:
        return n
    else:
        return n * fact_rec(n-1)


print(fact_rec(N))


# 2. DP (recursive)
def fact_dp_rec(n):
    if n == 1:
        return memo[n]
    else:
        if memo[n] == 0:
            memo[n] = n * fact_dp_rec(n-1)
        return memo[n]


memo = [0] * (N+1)
memo[1] = 1
print(fact_dp_rec(N))


# 3. DP (iterative)
# 내부 테이블을 생성하고
# for문을 도는 것이 핵심임
def fact_dp_iter(n):
    if n < 3:
        return n

    f = [0] * (n+1)
    f[1] = 1
    f[2] = 2
    for i in range(3, n+1):
        f[i] = i * f[i-1]
    return f[n]


print(fact_dp_iter(N))