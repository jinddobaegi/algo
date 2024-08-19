import sys
sys.stdin = open("week23/11066/11066.txt")
input = sys.stdin.readline
import heapq

# def min_cost_to_merge_files(file_sizes):
#     heapq.heapify(file_sizes)
#     total_cost = 0

#     while len(file_sizes) > 1:
#         first = heapq.heappop(file_sizes)
#         second = heapq.heappop(file_sizes)
#         cost = first + second
#         total_cost += cost
#         heapq.heappush(file_sizes, cost)

#     return total_cost

# def main():
#     T = int(input())
#     results = []
#     for _ in range(T):
#         K = int(input())
#         file_sizes = list(map(int, input().split()))
#         result = min_cost_to_merge_files(file_sizes)
#         results.append(result)
    
#     for result in results:
#         print(result)

# if __name__ == "__main__":
#     main()

# def merge_files(file_sizes):
    

# def main():
#     T = int(input())
#     result = []
#     for _ in range(T):
#         K = int(input())
#         file_sizes = list(map(int, input().split()))
#         dp = [[0] * (K) for _ in range(K)] 
#         # print(dp)
#         prefix = [0]
#         count = 0
#         for i in range(K):
#             count += file_sizes[i]
#             prefix.append(count)
#         print(prefix)
        
#         merge_files(file_sizes)


# if __name__ == "__main__":
#     main()

import sys
input = sys.stdin.readline

def merge_files(file_sizes):
    K = len(file_sizes)
    dp = [[0] * K for _ in range(K)]
    for i in dp:
        print(i)
    prefix_sum = [0] * (K + 1)

    for i in range(K):
        prefix_sum[i + 1] = prefix_sum[i] + file_sizes[i]

    for length in range(2, K + 1):  
        for i in range(K - length + 1):
            j = i + length - 1
            dp[i][j] = float('inf')
            for k in range(i, j):
                print("cost = dp[",i,"]","[",k,"] + dp[", k + 1,"][",j,"] + prefix_sum[",j + 1,"] - prefix_sum[",i,"]" )
                cost = dp[i][k] + dp[k + 1][j] + prefix_sum[j + 1] - prefix_sum[i]
                dp[i][j] = min(dp[i][j], cost)
                print("dp[i][j]=",dp[i][j], "min(","dp[i][j]=",dp[i][j],",cost=",cost)

    return dp[0][K - 1]

def main():
    T = int(input())
    results = []
    for _ in range(T):
        K = int(input())
        file_sizes = list(map(int, input().split()))
        
        result = merge_files(file_sizes)
        results.append(result)
    
    for result in results:
        print(result)

if __name__ == "__main__":
    main()
