import sys
sys.stdin = open("week22/11053/11053.txt")
input = sys.stdin.readline

# N = int(input())

# graph = list(map(int, input().split()))

# graph.sort()
# # print(graph)

# makelist = [0]
# for i in range(N):
#     num = graph[i]
#     if num > makelist[-1]:
#         makelist.append(num)
#     continue

# print(len(makelist)-1)




N = int(input())
numlist = [1] * N

graph = list(map(int, input().split()))
print(numlist)

for i in range(1, N):
    for j in range(i):
        if graph[i] > graph[j]:
            numlist[i] = max(numlist[i], numlist[j] + 1)

print(max(numlist))
    
    
