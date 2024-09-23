import sys
sys.stdin = open("week29/1806/1806.txt")
input = sys.stdin.readline
from collections import deque


N, S = map(int, input().split())

# 연속된 수들의 부분합 중에 그합이 S 이상인 것중에 가장 짧은 것의 길이
board = list(map(int, input().split()))

def cal(st):
    queue = deque([st])  
    count = float('inf')  
    
    while queue:
        start = queue.popleft() 
        temp_sum = board[start] 
        tmp_count = 1  
        
        for i in range(start + 1, N):
            temp_sum += board[i]
            tmp_count += 1
            
            if temp_sum >= S:
                count = min(count, tmp_count) 
                # print(count)
                break  
        
        if start + 1 < N:
            queue.append(start + 1)
    
    return count if count != float('inf') else 0

result = cal(0)
print(result)