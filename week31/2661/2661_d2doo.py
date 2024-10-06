# 좋은 수열
import sys
sys.setrecursionlimit(100000)

def check(x):
    for i in range(1, len(x)//2 + 1):
        if x[-i:] == x[-(i*2):-i]:
            return False
    else:
        return True

def sequence(x): # 수열 만들기
    global N
    if len(x) == N:
        print(x)
        exit()
    for i in '123':
        if check(x + str(i)):
            sequence(x + str(i))
    return


N = int(input())
sequence('1') # 가장 작은 수열
