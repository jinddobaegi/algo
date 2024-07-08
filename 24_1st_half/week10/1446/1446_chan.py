import sys
sys.stdin = open('week10/1446/1446.txt')
input = sys.stdin.readline
import heapq

def 최소거리다익스트라(시작노드):
    큐 = []
    heapq.heappush(큐, (0, 시작노드))
    거리[시작노드] = 0
    
    while 큐:
        가중치, 현재노드 = heapq.heappop(큐)

        if 거리[현재노드] == 가중치:
            break

        if 거리[현재노드] < 가중치:
            continue
        
        for 도착지, 거리값 in 그래프[현재노드]:
            새가중치 = 가중치 + 거리값
            if 새가중치 < 거리[도착지]:
                거리[도착지] = 새가중치
                heapq.heappush(큐, (새가중치, 도착지))
                
    
    

지름길개수, 고속도로길이 = map(int, input().split()) #  지름길개수는 12 이하인 양의 정수이고, 고속도로길이는 10,000보다 작거나 같은 자연수이다
최대길이 = 10000
거리 = [최대길이+1] * (최대길이+1)

그래프 = [[] for _ in range(최대길이+1)]
# print(그래프)

for _ in range(지름길개수):
    시작, 끝, 길이 = map(int, input().split())
    if 끝 > 고속도로길이:
        continue # continue가 읽히면 아래 코드는 실행되지 않고 다음 반복으로 넘어간다 
    그래프[시작].append((끝, 길이))
    
최소거리다익스트라(0)
print(거리[고속도로길이])

    

