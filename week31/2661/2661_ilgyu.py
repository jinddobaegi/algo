import sys
sys.stdin = open('input.txt')

n = int(input())

def find(x):
    x = str(x)
    k = len(x)
    for i in range(1, k // 2 + 1): # n자리 수 최대 절반
        # 절반
        if x[-i:] == x[-2*i:-i]: # sol함수에서 뒤쪽에 새로운 숫자를 붙이니까 뒤부터 검사
                                 # 반복검사 할때 뒤에서부터 함
            return False

        # if x[:i] == x[i:2*i]: # 얘도 절반 비교하는 거 같지만 이렇게하면 12111111 이런 케이스가 답으로 나와버림
        #     return False
    return True

# 1,2,3으로만 n자리 수열을 만들어서
def sol(num):
    if len(str(num)) == n:
        print(num)
        exit()
    else:
        for i in range(1, 4):
            if find(num*10 + i):
                sol(num*10 + i)

sol(1)
# 2023이랑 비슷함
