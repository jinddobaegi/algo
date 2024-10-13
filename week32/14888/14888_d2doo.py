# 연산자 끼워넣기
# 노가다..

def backtracking(idx, now):
    # max_v = -1e9  # -10억
    # min_v = 1e9  # 10억
    global min_v, max_v

    if idx == N - 1: # 종료조건
        max_v = max(now, max_v)
        min_v = min(now, min_v)
        return

    # 덧셈
    if operator[0] != 0:
        operator[0] -= 1 # 가능한 횟수를 빼주고
        backtracking(idx + 1, now + numbers[idx + 1])
        operator[0] += 1

    # 뺄셈
    if operator[1] != 0:
        operator[1] -= 1 # 가능한 횟수를 빼주고
        backtracking(idx + 1, now - numbers[idx + 1])
        operator[1] += 1

    # 곱셈
    if operator[2] != 0:
        operator[2] -= 1 # 가능한 횟수를 빼주고
        backtracking(idx + 1, now * numbers[idx + 1])
        operator[2] += 1

    # 나눗셈
    if operator[3] != 0:
        operator[3] -= 1 # 가능한 횟수를 빼주고
        if now < 0:
            # 음수를 나눴을 때 나머지가 있으면 몫에 + 1 됨 ㅠ
            # 그래서 양수로 만들고 다시 음수로 만들어주기!
            backtracking(idx + 1, -(-now // numbers[idx + 1]))
        else:
            backtracking(idx + 1, now // numbers[idx + 1])
        operator[3] += 1

    # return max_v, min_v

N = int(input())
numbers = list(map(int, input().split()))
operator = list(map(int, input().split()))
max_v = -1e9  # -10억
min_v = 1e9  # 10억
backtracking(0, numbers[0])

# ans1, ans2 = backtracking(0, numbers[0])
print(max_v)
print(min_v)