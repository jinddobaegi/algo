N = int(input())
nums = list(map(int, input().split()))
op = list(map(int, input().split())) # + - * /

max_res = int(-1e9)
min_res = int(1e9)

def dfs(idx, total):
    global max_res, min_res

    if idx == N:
        max_res = max(max_res, total)
        min_res = min(min_res, total)
        return

    if op[0]:  # (+)
        op[0] -= 1
        dfs(idx + 1, total + nums[idx])
        op[0] += 1
    if op[1]:  # (-)
        op[1] -= 1
        dfs(idx + 1, total - nums[idx])
        op[1] += 1
    if op[2]:  # (*)
        op[2] -= 1
        dfs(idx + 1, total * nums[idx])
        op[2] += 1
    if op[3]:  # (/)
        op[3] -= 1
        dfs(idx + 1, int(total / nums[idx]))
        op[3] += 1

dfs(1, nums[0])
print(max_res)
print(min_res)