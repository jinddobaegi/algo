import sys
sys.stdin = open("week31/2661/2661.txt")
# from itertools import product

# N = int(input())

# def good(seq):
#     n = N
#     for length in range(1, n // 2 + 1): # 반복될 길이들
#         for i in range(n - 2 * length + 1): # 시작점부터 끝점
#             if seq[i:i+length] == seq[i+length:i+2*length]:
#                 return False
#     return True


# nums = [1,2,3]
# perm = list(product(nums, repeat=N))

# nice = []

# for seq in perm:
#     if good(seq):
#         nice.append(seq)


# result = []

# minsum = 4*7
# index = -1
# for indec ,p in enumerate(nice):
#     if sum(p) < minsum:
#         minsum = sum(p)
#         index = indec

# print(''.join(map(str,nice[index])))

def good(seq):
    n = len(seq)
    for length in range(1, n // 2 + 1): # 반복될 길이들
        for i in range(n - 2 * length + 1): # 시작점부터 끝점
            if seq[i:i+length] == seq[i+length:i+2*length]:
                return False
    return True

def backtrack(seq, n):
    if len(seq) == n:
        print(''.join(map(str, seq)))
        exit()  # 가장 작은 수열을 찾으면 프로그램 종료
    
    for num in range(1, 4):  # 1, 2, 3을 사용
        seq.append(num)
        if good(seq):
            backtrack(seq, n)
        seq.pop()

N = int(input())
backtrack([], N)


