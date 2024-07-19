import sys
sys.stdin = open("week21/1715/1715.txt")
import heapq

def check(N):
    while N > 1:
        a = heapgraph.pop(0)
        print(a)

N = int(input())
heapgraph = []

for _ in range(N):
    heapq.heappush(heapgraph, int(input()))

result = 0
while len(heapgraph) > 1:
    a = heapq.heappop(heapgraph)
    b = heapq.heappop(heapgraph)
    absum = a + b
    result += absum
    heapq.heappush(heapgraph, absum)

print(result)


    
