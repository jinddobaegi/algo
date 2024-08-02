# 첫 줄에 물품의 수 N(1 ≤ N ≤ 100)과 준서가 버틸 수 있는 무게 K(1 ≤ K ≤ 100,000)가 주어진다.
# 두 번째 줄부터 N개의 줄에 거쳐 각 물건의 무게 W(1 ≤ W ≤ 100,000)와 해당 물건의 가치 V(0 ≤ V ≤ 1,000)가 주어진다.

# 입력으로 주어지는 모든 수는 정수이다.

# 출력
# 한 줄에 배낭에 넣을 수 있는 물건들의 가치합의 최댓값을 출력한다.

import sys
sys.stdin = open("week21/12865/12865.txt")
input = sys.stdin.readline

N, K = map(int, input().split())
chart = [[0,0]]
graph = [[0] * (K+1) for _ in range(N+1)] 

for _ in range(N):
    w, v = map(int, input().split())
    chart.append([w, v])


for i in range(1,N+1):
    for j in range(1,K+1):
        w = chart[i][0]
        v = chart[i][1]

        # print(w, v)
        if j < w: # 인덱스가 무게이다. w가 일치하지 않는경우 그 아래는 모두 그전무게를 넣는다. 
            graph[i][j] = graph[i-1][j]
        else:
            graph[i][j] = max(graph[i-1][j], v + graph[i-1][j-w])
#graph = [[0, 0, 0, 0, 0, 0, 0, 0],  무게 인덱스를 위해 처음은 없게 설정 K = 7
         #[0, 0, 0, 0, 0, 0, 13, 13],   첫번째가 6, 13 이기때문에/ 이물건을 넣었을 경우 1개 넣을 수 있고 최대 13가치이다.
         #[0, 0, 0, 0, 8, 8, 13, 13],   두번째는 4, 8 이며 / 무게 4에서 8의 가치를 가지며 / 전꺼와 비교했을때 전이 더 크기 때문에 13을 넣는다.
         #[0, 0, 0, 6, 8, 8, 13, 14],   세번째는 3, 6 이며 / 무게 3에서 6의 가치를 가지고 / 위와 동일하게 움직인 다음에 마지막에 j - w = 7 - 3의 가치와 더해준다. / j - w 인 이유는 if 문 참고
         #[0, 0, 0, 6, 8, 12, 13, 14]]  마지막은 5, 12 이며 / 무게 5에서 12의 가치를 가진다. / 위와 동일하게 움직이나 맥스값에 도달하지 못한다.

print(graph[N][K])