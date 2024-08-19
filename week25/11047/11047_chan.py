import sys
sys.stdin = open("week25/11047/11047.txt")
input = sys.stdin.readline
from collections import deque

N, M = map(int, input().split())
coin_list = deque()
count = 0

for _ in range(N):
    coin_list.append(int(input()))

coin_list.reverse()  

def count_coin():
    global count, M 

    while coin_list and M > 0: 
        money = coin_list.popleft()

        if money <= M: 
            count += M // money  
            M %= money  

count_coin()
print(count)