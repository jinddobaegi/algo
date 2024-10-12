import sys
sys.stdin = open("week32/14888/14888.txt")
from itertools import permutations

#덧셈(+)의 개수, 뺄셈(-)의 개수, 곱셈(×)의 개수, 나눗셈(÷)의 개수 0 0 1 0

# 숫자는 순서대로니까 연산자의 순열로

# 최대 최소의 값 구하기

N = int(input())
num_list = list(map(int, input().split()))

operators = list(map(int, input().split()))

can_oper = []
oper = ["+","-","*","/"]

for i in range(4):
    can_oper.extend([oper[i]] * operators[i])  # 연산자 추가

oper_permutations = set(permutations(can_oper))    

def cal2(a, b, oper):
    if oper == '+':
        return a + b
    elif oper == '-':
        return a - b
    elif oper == '*':
        return a * b
    elif oper == '/':
        if a < 0:
            return -(-a // b)
        else:
            return a // b

def cal():
    max_num = float("-inf")  
    min_num = float("inf")

    for per in oper_permutations:
        result = num_list[0]

        for i in range(1, N):
            result = cal2(result, num_list[i], per[i - 1])

        max_num = max(max_num, result)
        min_num = min(min_num, result)

    return max_num, min_num

max_num, min_num = cal()

print(max_num)
print(min_num)








