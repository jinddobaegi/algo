import sys
sys.stdin = open("week30/11729/11729.txt")
from collections import deque

N = int(input())

numlst = deque([i for i in range(1, N +1)])
table = [numlst, deque(), deque()]

print(2**N -1)
def hanoi(n, start, target, midle):
    if n == 1:
        print(start, target)
        return
    
    hanoi(n-1, start, midle, target)
    
    print(start, target)
    
    hanoi(n-1, midle, target, start)

hanoi(N, '1', '3', '2')