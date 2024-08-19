import sys
sys.stdin = open("week24/1080/1080.txt")    
def metrix(node):
    if 0 <= node + 3 < M and 0 <= node + 3 < M:
        for i in range(3):
            for j in range(3):
                new1 = node + i
                new2 = node + j
                if one[new1][new2] == 1:
                    one[new1][new2] = 0
                else:
                    one[new1][new2] = 1
            
def check(start):
    while start < M:
        if one != two:
            for i in range(M):
                if one[i][start] != two [i][start]:
                    metrix(start)
            check(start + 1)
            

N, M = map(int, input().split())

one = [list(map(int, list(input().strip()))) for _ in range(N)]
for i in one:
    print(i)
print()
# two = list(input()for _ in range(N))
two = [list(map(int, list(input().strip()))) for _ in range(N)]
for i in two:
    print(i)

start = 0
check(start)

