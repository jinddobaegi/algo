import sys
sys.stdin = open('input.txt')
from itertools import permutations

n = int(input())
arr = list(map(int, input().split()))
oper = list(map(int, input().split()))
# +, -, x, % 수

# oper = [0, 0, 1, 0]
cases = []
while oper != [0, 0, 0, 0]:
    if oper[0] != 0:
        oper[0] -= 1
        cases.append("+")
    elif oper[1] != 0:
        oper[1] -= 1
        cases.append("-")
    elif oper[2] != 0:
        oper[2] -= 1
        cases.append("x")
    else:
        oper[3] -= 1
        cases.append("%")

perm = set(permutations(cases, n-1))

max_v = -float('inf')
min_v = float('inf')

for case in perm: # 362만
    # print(case)
    temp = arr[0]
    # 연산자 하나 꺼내고 다음 수 꺼내고
    for i in range(n-1): # 최대 10
        if case[i] == "+":
            temp = temp + arr[i+1]
        elif case[i] == "-":
            temp = temp - arr[i+1]
        elif case[i] == "x":
            temp = temp * arr[i+1]
        else:
            if temp < 0:
                temp = ((-1 * temp) // arr[i+1]) * -1
            else:
                temp = temp // arr[i+1]

    max_v = max(max_v, temp)
    min_v = min(min_v, temp)


print(max_v)
print(min_v)
